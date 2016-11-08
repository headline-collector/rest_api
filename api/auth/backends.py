__author__ = 'wangyi'
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib.auth.models import AnonymousUser
from ..utils.auth_utils import app_secret_coder, check_sign_sim
from django.core.cache import cache
from exceptions import *


def config_applicatoin():
    """
    Returns the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_APPLICATION)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )


# signature auth
class QueryBackend(object):

    PK = 'key'

    def get_app(self, _pk):
        Application = config_applicatoin()
        try:
            app = Application.objects.select_related().get(**{self.PK: _pk})
            return app
        except Application.DostNotExist:
            return AnonymousUser()

    def authenticate(self, _pk=None, sign_req=None, signature_string=None, algorithm=None):
        if self.verify_signature(_pk, sign_req):
            return self.check_user(_pk, sign_req, signature_string, algorithm)
        else:
            # when exception enabled, this sentence will never be executed
            # I am considering to remove the sentence
            return AnonymousUser()

    def verify_signature(self, _pk, sign_req):
        sign_used = cache.get(_pk)
        if sign_used is None:
            return True
        if self._cmp_signature(sign_req, sign_used):
            # return False
            raise MultiReq_Exception()
        else:
            return True

    def check_user(self, _pk=None, sign_req=None, signature_string=None, algorithm=None):
        app = self.get_app(_pk)
        user = app.user
        app_secret = app.secret.encode("ascii")#user.app_secret.encode("ascii")

        sign_srv = app_secret_coder(app_secret, signature_string.encode("ascii"))

        if self._cmp_signature(sign_req, sign_srv):
            # _pk should not be updated
            cache.set(_pk, sign_req)
            user.last_signed = sign_req
            return user

        else:
            # return AnonymousUser()
            raise SignatureFailed_Exception(detail="Signature Failed!")

    def _cmp_signature(self, sign_req, sign_srv):
        return check_sign_sim(sign_req, sign_srv)





