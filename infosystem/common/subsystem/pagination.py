from typing import Any, Type, Optional
from sqlalchemy.sql import text
from infosystem.common import exception


class Pagination(object):

    def __init__(self, page: Optional[int], page_size: Optional[int],
                 order_by: Optional[str]) -> None:
        self.page = page
        self.page_size = page_size
        self.order_by = order_by

    @classmethod
    def getPagination(cls, resource: Type[Any], **kwargs):
        page = kwargs.pop('page', None)
        page = int(page) if page is not None else None
        page_size = kwargs.pop('page_size', None)
        page_size = int(page_size) if page_size is not None else None
        order_by = kwargs.pop('order_by', None)

        name_pagination_column = 'pagination_column'

        if order_by is None and hasattr(resource, name_pagination_column):
            order_by = getattr(resource, name_pagination_column)

        return cls(page=page, page_size=page_size, order_by=order_by)

    def applyPagination(self, query):
        if (self.order_by is not None and self.page is not None
                and self.page_size is not None):
            query = query.order_by(text(self.order_by))

        if self.page_size is not None:
            if self.page_size < 0:
                raise exception.BadRequest(
                    'page_size must be greater than or equal to zero.')
            query = query.limit(self.page_size)
            if self.page is not None:
                if self.page < 0:
                    raise exception.BadRequest(
                        'page must be greater than or equal to zero.')
                query = query.offset(self.page * self.page_size)

        return query
