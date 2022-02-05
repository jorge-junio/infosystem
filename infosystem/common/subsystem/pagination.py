from typing import Any, Type, Optional


class Pagination(object):

    def __init__(self, page: Optional[int], page_size: Optional[int],
                 order_by: Optional[str]) -> None:
        self.page = page
        self.page_size = page_size
        self.order_by = order_by
    
    @classmethod
    def getPagination(cls, resource: Type[Any], args):
        page = args.pop('page', None)
        page = int(page) if page is not None else None
        page_size = args.pop('page_size', None)
        page_size = int(page_size) if page_size is not None else None
        order_by = args.pop('order_by', None)

        name_pagination_column = 'pagination_column'

        if order_by is None and hasattr(resource, name_pagination_column):
            order_by = getattr(resource, name_pagination_column)

        return cls(page=page, page_size=page_size, order_by=order_by)

    def applyPagination(self, query):
        if order_by is not None and page is not None and page_size is not None:
            query = query.order_by(text(order_by))

        if page_size is not None:
            query = query.limit(page_size)
            if page is not None:
                query = query.offset(page * page_size)
                
        return query