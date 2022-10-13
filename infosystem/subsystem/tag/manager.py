from infosystem.common.subsystem.pagination import Pagination
from infosystem.common.subsystem import manager, operation
from infosystem.common import exception


class GetTagsFromEntity(operation.List):

    def pre(self, **kwargs):
        self.entity_name = kwargs.get('entity_name', None)
        self.domain_id = kwargs.get('domain_id', None)
        if not self.entity_name or not self.domain_id:
            raise exception.BadRequest(
                'entity_name and domain_id are required')
        return True

    def do(self, session, **kwargs):
        sql_query = (
            'SELECT DISTINCT UNNEST(STRING_TO_ARRAY(tag, \' \')) as tag'
            ' FROM {} WHERE domain_id=\'{}\' ORDER BY tag')

        page = kwargs.get('page', None)
        page_size = kwargs.get('page_size', None)

        if page and page_size:
            sql_query += (f' LIMIT {page_size} OFFSET {page}')

        rs = session.execute(sql_query.format(self.entity_name, self.domain_id))
        response = [r._mapping['tag'] for r in rs]

        return response


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.get_tags_from_entity = GetTagsFromEntity(self)
