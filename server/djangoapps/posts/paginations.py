from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.response import Response


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 2

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data
        })

class PostPageNumberPagination(PageNumberPagination):
    page_size = 4

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
