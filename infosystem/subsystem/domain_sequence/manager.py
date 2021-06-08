from uuid import uuid4
import uuid

from infosystem.common.subsystem import operation, manager

from infosystem.subsystem.domain_sequence.resource import DomainSequence


class GetNextVal(operation.Operation):
    def pre(self, session, id, name, step, **kwargs):
        self.id = id
        self.name = name
        self.step = int(step)
        self.entity = session.query(DomainSequence)\
            .filter(DomainSequence.name == self.name)\
            .filter(DomainSequence.domain_id == self.id)\
            .all()

        return super().pre(session=session)

    def do(self, session, **kwargs):
        if not self.entity:
            return self.create_domain_sequence(kwargs)

        nextval = self.entity[0].nextval(self.step)

        super().do(session=session, **kwargs)

        return nextval

    def create_domain_sequence(self, kwargs) -> int:
        kwargs['id'] = uuid4().hex
        kwargs['domain_id'] = self.id
        kwargs['value'] = self.step
        kwargs.pop('step', None)

        self.manager.create(**kwargs)

        return self.step


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.get_next_val = GetNextVal(self)
