from rest_framework import pagination


class MessagePagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
