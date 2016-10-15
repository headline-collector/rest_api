__author__ = 'wangyi'

from rest_framework import HTTP_HEADER_ENCODING, exceptions
# this will use the authenticate backend specied in the setting project
from django.contrib.auth import authenticate
import inspect
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from .exceptions import *
from .decorators import handle_err
import re
import logging
from api.auth.backends import QueryBackend
from dateutil import parser

AUTHORIZATION = 'Authorization'

logger = logging.getLogger(__name__)

def url_encode(url, args):
    args_proc = lambda o: \
        '='.join([o[0],str(o[1])]) if isinstance(o, tuple) else str(0)
    map_ob = map(lambda it: args_proc(it), args)
    return '?'.join([url,'&'.join(map_ob)])

def get_args(r):
#    r = req_v.request
    return r.__getattribute__(r.method)


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
    """
    PREFIX = "HTTP_"
    AUTHORIZATION_HEADER = "Authorization"

    SIGNATURE_RE = re.compile('signature="(.+?)"')
    SIGNATURE_HEADERS_RE = re.compile('headers="([\(\)\sa-z0-9-]+?)"')


    def parse_header(self, auth_header, request):
        """
        sign5 scheme:

        digest: 'Signature algorithm'=xx:
        Date: xxxx-xx-xx

        :return:
        or raise exception('authri handler not matched!')
        with hints header should be added at least
            Signature: keyId="rsa-key-1",algorithm="rsa-sha256",
            headers="(request-target) host date digest content-length",
            signature="Base64(RSA-SHA256(signing string))"

        """
        param = {}
        mtch = self.SIGNATURE_HEADERS_RE.search(auth_header)
        if mtch is None:
            sign_headers = ['Date']
        else:
            sign_headers = mtch.group(1).split()

        # all the parameters passed used for signing url
        for h in sign_headers:
            if h == '(request-target)':
                continue
            content = request.META.get(self.to_header(h))
            param[h] = content

        # obtain a sign_url for signature
        method = request.META.get(self.to_header('request-method'))
        host = request.META.get(self.to_header('host'))
        path = request.META.get('PATH_INFO')
        sign_url_template = "{:method} {:host}:{:path}".format(method=method,host=host,path=path)

        param['URL'] = url_encode(sign_url_template, list(param.items()))

        mtch = self.SIGNATURE_RE.search(auth_header)
        if mtch is None:
            raise NotAuthenticated('Signature Missed!')
        param['signature'] = mtch.group(1)
        return param


    def to_header(self, header_str):
        """
        With the exception of CONTENT_LENGTH and CONTENT_TYPE, as given above,
        any HTTP headers in the request are converted to META keys by converting all characters to uppercase,
        replacing any hyphens with underscores and adding an HTTP_ prefix to the name.
        :param headers_str:
        :return: header_name
        # https://docs.djangoproject.com/en/1.6/ref/request-response/#django.http.HttpRequest.META
       """
        header_name = header_str.lower()
        if header_name == 'content-type':
            return 'CONTENT-TYPE'
        elif header_name == 'content-length':
            return 'CONTENT-LENGTH'
        return self.PREFIX + '_'.join(header_name.split('-'))


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


class SignatureAuthentication(BaseAuthentication):

    @handle_err
    def authenticate(self, request):
        """
        get header info

        assign a user to request or raise an error
        the error should be handled in corresponding
        middleware, view or decorator
        the auth will provide different strategies utils
        """
        param = {}

        auth_header = request.META.get('Authorization', None)

        authd = get_args(request) if auth_header is None \
               else self.parse_header(auth_header, request)

        try:
            param['pk'] = authd['id'] # authd.get('APP_KEY')
        except KeyError:
            raise NotAuthenticated('id not found!')
        try:
            param['sign_req'] = authd['signature'] # authd.get('signature')
        except KeyError:
            raise NotAuthenticated('signature not found!')
        param['URL'] = authd['request_target'] # authd.get('request_target')

        try:
            obj = parser.parse(authd.get('Date','')) # authd.get('Date', None)
            param['t_str'] = '' if obj is None else obj.strftime('%Y-%m-%d') #optional
        except ValueError:
            param['t_str'] = authd.get('Date', '')

        developer = self.authenticate_credentials(**param)
        return developer, param['pk']

    def authenticate_header(self, request):pass

    def authenticate_credentials(self, **credentials):
        """
        Signing HTTP Messages draft-cavage-http-signature-signatures-o3
        :param credentials:
        :return:
        """
        try:

            inspect.getcallargs(QueryBackend.authenticate, credentials)
        except TypeError as err:
            message = err.message
            logger.error(message)
            raise Func_Exception(message)

        return authenticate(**credentials)

