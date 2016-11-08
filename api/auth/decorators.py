__author__ = 'wangyi'
from rest_framework.exceptions import NotAuthenticated
import logging

# this __name__ has not been activated in LOGGING config
logger = logging.getLogger(__name__)

def handler_authentication(func):

    def wrapper(self, request):
        try:
            user, token = func(self, request)
        except Exception as err:
            try:
                detail = err.detail
            except AttributeError:
                logger.error(err.message)
                raise NotAuthenticated(err.message)
            else:
                logger.error(detail)
                raise NotAuthenticated(detail)

        return user, token

    return wrapper