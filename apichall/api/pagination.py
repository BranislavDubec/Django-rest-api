from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    default_limit = 50
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50
    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'count': self.count,
                'limit': self.limit,
                'offset': self.offset
            },
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data
            })