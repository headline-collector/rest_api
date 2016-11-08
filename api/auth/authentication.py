__author__ = 'wangyi'

# this will use the authenticate backend specified in the setting project
from django.contrib.auth import _get_backends, _clean_credentials
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.middleware.csrf import CsrfViewMiddleware
import inspect
try:
   set
except NameError:
   from sets import Set as set
from collections import OrderedDict
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.authtoken.models import Token
from .exceptions import *
import logging
from api.auth.signals import user_signing, user_false_singed, user_signed
import base64
import api.utils.tokenTab as TokenTab
import api.utils.operator as Operator

AUTHORIZATION = 'HTTP_AUTHORIZATION'

logger = logging.getLogger(__name__)

def url_encode(url, args):
    args_processor = lambda o: \
        '='.join([o[0],str(o[1])]) if isinstance(o, tuple) else str(o)
    map_ob = map(lambda it: args_processor(it), args)
    return '?'.join([url,'&'.join(map_ob)])

def get_args(req):
    """
    :param req: django-rest Request obj
    :return: params
    """
    return req.__getattribute__(req.method)

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get(AUTHORIZATION, b'')
    if isinstance(auth, type('')):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

# This authentication imeplements WBY auth workflow specified by
# document:
class BaseAuthentication(object):
    """
    All authentication classes should extend BaseAuthentication.
    Authorization header defined in RFC2617 : credentials = auth-scheme #auth-param
     First Response Header:
        WWW-Authenticate: {support algos}
        realm= ""
        ...
        nonce= {base64 codes}
        Response code 401

     Second round:
        Authorization: {method}(we need to parse)
        once: {base64 codes}
        cnonce: {base64 codes}
        digest: xxxx
        ...
    """
    PROTOCOL = {
        'PREFIX': 'HTTP_',

    }

    www_realm = "api"

    def to_header(self, header_str):
        """
        With the exception of CONTENT_LENGTH and CONTENT_TYPE, as given above,
        any HTTP headers in the request are converted to META keys by converting all characters to uppercase,
        replacing any hyphens with underscores and adding an HTTP_ prefix to the name.
        :param headers_str:
        :return: header_name
        # https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.META
       """
        header_name = header_str.upper()
        if header_name == 'content-type':
            return 'CONTENT-TYPE'
        elif header_name == 'content-length':
            return 'CONTENT-LENGTH'
        return self.PROTOCOL['PREFIX'] + '_'.join(header_name.split('-'))


    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        raise NotImplementedError(".authenticate() must be overridden.")

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        This will be handled automatically by django_rest.view.dispatch method
        """
        raise NotImplementedError(".authenticate_header() must be overriden")

    def authenticate_credentials(self, **credentials):
        """
        return user to be used by APIView controller
        """
        raise NotImplementedError(".authenticate_credentials() must be overridden")


class SignatureAuth(BaseAuthentication):

    # according to the protocol, they should be in lower case, separated by ascii space ' '
    # must have '(request-target)', 'date' and optional contain 'content-length', 'digest'
    # this portion can be configured in settings
    www_headers = ('(request-target)', 'host', 'date',)

    def authenticate(self, req):
        """
        This implementation verifies the Signature:
        https://www.ietf.org/archive/id/draft-cavage-http-signatures-05 Chapter 2.5.(Verifying a Signature)
        """
        auth = get_authorization_header(req).split(' ', 1)
        # check the auth scheme
        if not auth or auth[0].lower() != b'signature':
            return None
        # auth = get_authorization_header(req)
        # # check the auth scheme
        # if not auth or not auth.startswith('Signature'):
        #     return None


        # keyId, algorithm, signature, signed_headers = self.parse_auth(req, auth[10:])
        keyId, algorithm, signature, signed_headers = self.parse_auth(req, auth[1])
        signature_string = self.compose_signature(req, signed_headers)

        # HMAC
        user, token = self.authenticate_credentials(_pk=keyId, sign_req=signature, signature_string=signature_string, algorithm=algorithm)
        return (user, token)


    def parse_auth(self, req, auth_repr):
        """
        This implementation extract necessary components to construct signautre from server side
        Signing HTTP Messages draft-cavage-http-signature-signatures-05 Chapter 3.1(Authroization Header)
        parse `headers` in `auth_repr`
        :return: `keyId`, `algorithm`, base64 decoded `signature` and `signed_headers`
        """
        auth_param = {}
        for item in auth_repr.split(TokenTab.ASCII_COMMA):
            try:
                key, val = item.split(TokenTab.ASCII_EQ, 1)
                auth_param[key.strip()] = val[1:-1]
            except Exception as e:
                raise(e)

        keyId = auth_param.get('key', None)
        algorithm = auth_param.get('algorithm', None)
        signature = auth_param.get('signature', None)
        headers = auth_param.get('headers', None)

        if None in (keyId, signature, headers):# `algorithm` has default value
            raise BAD_SIGN("Bad signature, expected: keyId, algorithm, signatures, headers!")

        if headers is not None:
            headers = headers.split()

        if (headers is not None) and not \
                Operator.belong(('(request-target)', 'date'), headers):
            raise BAD_SIGN("headers in Authorization Header is in wrong format!")

        # order is important
        signed_headers = OrderedDict()
        for header in headers[1:-1]:
            if signed_headers.get(header) is None:
                # Rule also require to concatenate the values in the under the same key
                signed_headers[header.strip()] = req.META.get(self.to_header(header.strip()))
        signed_headers['Date'] = req.META.get(self.to_header('Date'))

        return keyId, algorithm, signature, signed_headers


    def compose_signature(self, req, signed_headers):
        """
        Signing HTTP Messages draft-cavage-http-signature-signatures-05 Chapter 2.3(Construct a Signature)
        :return: `signature string`
        """
        signature_string = "(request-target): {method} {path}\n{ret}"
        method = req.method.lower()
        path = req.get_full_path()

        def encode_signed_headers(signed_headers):
            # Signing HTTP Messages draft-cavage-http-signature-signatures-05 Rule 2.3.2

            args_processor = lambda (key, val): \
                ': '.join((key.lower(), ', '.join(val) )) if isinstance(val, (list, tuple)) and len(val) > 1 else \
                ': '.join((key.lower(), val[0] if isinstance(val, (list, tuple)) else val))
            map_ob = map(args_processor, signed_headers.items())
            return '\n'.join(map_ob)

        ret = encode_signed_headers(signed_headers)
        return signature_string.format(method=method, path=path, ret=ret)

    def authenticate_credentials(self, **credentials):
        """
        If the given credentials are valid, return a User object.
        """
        for backend, backend_path in _get_backends(return_tuples=True):
            try:
                inspect.getcallargs(backend.authenticate, **credentials)
            except TypeError:
                # This backend doesn't accept these credentials as arguments. Try the next one.
                continue

            try:
                user = backend.authenticate(**credentials)
            except PermissionDenied:
                # This backend says to stop in our tracks - this user should not be allowed in at all.
                return None
            if user is None:
                continue
            # Annotate the user object with the path of the backend.
            user.backend = backend_path
            token = Token.objects.get_or_create(user=user)
            # TO Do: check expiration

            return (user, token)

        # The credentials supplied are invalid to all backends, fire signal
        user_false_singed.send(sender=__name__,
                credentials=_clean_credentials(credentials))

    def authenticate_header(self, request):
        """
        This implementation initiates Signature Authentication:
        Signing HTTP Messages draft-cavage-http-signature-signatures-05 Chapter 3.1.1(Verifying a Signature)
        """
        return 'Signature realm={www_realm},headers="{www_headers}"'.format(www_realm=self.www_realm, www_headers=TokenTab.ASCII_SPACE.join(self.www_headers))


