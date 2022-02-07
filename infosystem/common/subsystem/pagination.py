from typing import Any, Type, Optional
from infosystem.common import exception
from infosystem.common.exception import BadRequest


class Pagination(object):

    def __init__(self, page: Optional[int], page_size: Optional[int],
                 order_by: Optional[str]) -> None:
        self.page = page
        self.page_size = page_size
        self.order_by = order_by

    @classmethod
    def get_pagination(cls, resource: Type[Any], **kwargs):
        try:
            page = kwargs.pop('page', None)
            page = int(page) if page is not None else None
            page_size = kwargs.pop('page_size', None)
            page_size = int(page_size) if page_size is not None else None
            order_by = kwargs.pop('order_by', None)

            name_pagination_column = 'pagination_column'

            if order_by is None and page is not None and page_size is not None \
                    and hasattr(resource, name_pagination_column):
                order_by = getattr(resource, name_pagination_column)

            if page_size is not None and page_size < 0:
                raise exception.BadRequest(
                    'page_size must be greater than or equal to zero.')
            if page is not None and page < 0:
                raise exception.BadRequest(
                    'page must be greater than or equal to zero.')

            cls._validate_order_by(order_by, resource)
        except BadRequest as br:
            raise exception.BadRequest(br.message)
        except ValueError:
            raise exception.BadRequest('page or page_size is invalid')

        return cls(page=page, page_size=page_size, order_by=order_by)

    def _validate_order_by(order_by: Optional[str], resource: Type[Any]):
        if order_by is None:
            return None
        order_by_post_split = order_by.split(',')
        for i in order_by_post_split:
            itemAux = i.strip().split(' ')
            for j in itemAux:
                if (j != 'desc' and j != 'asc' and j != '' and not hasattr(resource, j)):
                    raise exception.BadRequest(
                        'order_by is invalid.')
