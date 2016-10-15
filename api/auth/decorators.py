__author__ = 'wangyi'
from rest_framework.exceptions import NotAuthenticated
import logging

logger = logging.getLogger(__name__)

def handle_err(func):

    def wrapper(self, request):
        try:
            developer, app_key = func(self, request)
        except Exception as err:
            try:
                detail = err.detail
            except AttributeError:
                logger.error(err.message)
                raise NotAuthenticated(err.message)
            else:
                logger.error(detail)
                raise NotAuthenticated(detail)

        return developer, app_key

    return wrapper