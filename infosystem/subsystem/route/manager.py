from typing import List
from infosystem.common.exception import InfoSystemException

from infosystem.common.subsystem import operation, manager
from infosystem.subsystem.route.resource import Route


class CreateRoutes(operation.Operation):

    def pre(self, routes: List[Route], session, **kwargs) -> bool:
        self.routes = routes
        return True

    def do(self, session, **kwargs) -> List[Route]:
        session.bulk_save_objects(self.routes)
        return self.routes


class TestGet(operation.Operation):

    def do(self, session, **kwargs):
        users_total = []
        domains = self.manager.api.domains().list(name='viggo')
        for domain in domains:
            domain.display_name += 'a'
            self.manager.api.domains().update(**{ 'id': domain.id, 'display_name': domain.display_name})
            users = self.manager.api.users().list(domain_id=domain.id)
            for user in users:
                if user.nickname is not None:
                    user.nickname += 'b'
                self.manager.api.users().update(**{ 'id': user.id, 'nickname': user.nickname})
            users_total += users
        raise InfoSystemException("asdas")
        return users_total


class Manager(manager.Manager):

    def __init__(self, driver):
        super().__init__(driver)
        self.create_routes = CreateRoutes(self)
        self.tests = TestGet(self)
