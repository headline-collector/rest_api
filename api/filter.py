__author__ = 'wangyi'

from rest_framework import filters

class OrderBy_ky(filters.OrderingFilter):

    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = self.remove_invalid_fields(queryset, fields, view)
            if ordering:
                return ordering

        # No ordering was included, or all the ordering fields were invalid
        return self.get_default_ordering(view)

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            return queryset.order_by(*ordering)
        return queryset
