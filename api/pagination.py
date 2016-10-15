__author__ = 'wangyi'

from rest_framework.pagination import PageNumberPagination

class WBYAPI_Pagination(PageNumberPagination):

    def get_paginated_response(self, data):
        pass

