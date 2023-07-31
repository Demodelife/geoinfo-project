from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """
    Custom Pagination Class.
    """
    page_size_query_param = 'count'

    def get_paginated_response(self, data):
        """
        Method overrides paginated response.
        Sets a new value for the page size if specified in the search.
        """
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_count': self.page.paginator.count,
            'page_size': int(self.request.query_params.get('count', 0)) or self.page_size,
            'results': data
        })
