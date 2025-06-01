from rest_framework.pagination import CursorPagination


class SafeCursorPagination(CursorPagination):
    page_size = 6
    ordering = '-created_at'
    cursor_query_param = 'cursor'


class TaskCursorPagination(CursorPagination):
    page_size = 5
    ordering = '-created_at'