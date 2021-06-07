from infosystem.common.subsystem import operation, manager

from infosystem.subsystem.domain_sequence.resource import DomainSequence


class GetNextVal(operation.Operation):
    def pre(self, session, id, name, **kwargs):
        self.id = id
        self.name = name

        return super().pre(session=session)

    def do(self, session, **kwargs):
        return DomainSequence.nextval(session, self.id, self.name)


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.get_next_val = GetNextVal(self)
