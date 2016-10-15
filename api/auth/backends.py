__author__ = 'wangyi'

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from ..utils.auth_utils import app_secret_coder, check_sign_sim
from ..utils.auth import secret_coder
from django.core.cache import cache
from exceptions import *


# signature auth
class QueryBackend(object):

    PK = 'id'

    def get_user(self, _pk):
        AppModel = get_user_model()
        try:
            # __code = "AppModel.objects.get({0}=_pk)".format(self.PK)
            # app = None
            # exec(__code)
            # return app
            app = AppModel.objects.get(id=_pk)
            return app
            # developer = AppModel.objects.get(pk=_pk)
        except AppModel.DostNotExist:
            return AnonymousUser()

    def authenticate(self, pk=None, sign_req=None, URL=None, t_str=None):
        if self.verify_effective(pk, sign_req):
            return self.check_user(pk, sign_req, URL, t_str)
        else:
            # when exception enabled, this sentence will never be executed
            return AnonymousUser()

    def verify_effective(self, app_key, sign_req):
        sign_used = cache.get(app_key)
        if sign_used is None:
            return True
        if self._cmp_signature(sign_req, sign_used):
            # return False
            raise MultiReq_Exception()
        else:
            return True

    def check_user(self, pk=None, sign_req=None, URL=None, t_str=None):

        app = self.get_user(pk)

        app_secret = app.app_secret

        # sign_srv = app_secret_coder(str(app_secret), "GET {URL}/?{DATE}".format(URL=URL, DATE=t_str))
        sign_srv = secret_coder(str(app_secret), 'GET', str(URL), t_str)

        if True:#self._cmp_signature(str(sign_req), sign_srv):
            # api_key should not be updated
            cache.set(pk, sign_req)

            app.token = sign_req
            return app

        else:
            # return AnonymousUser()
            raise SignatureFailed_Exception(detail="Signature Failed!")

    def _cmp_signature(self, sign_req, sign_srv):
        return check_sign_sim(sign_req, sign_srv)





