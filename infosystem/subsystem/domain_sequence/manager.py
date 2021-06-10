from sqlalchemy import text

from infosystem.common.subsystem import operation, manager


class GetNextVal(operation.Operation):
    def pre(self, session, id, name, **kwargs):
        self.domain_id = id
        self.name = name

        return super().pre(session=session)

    def do(self, session, **kwargs):
        sql_text = text('SELECT domain_seq_nextval(:domain_id, :name)')

        return session.execute(
            sql_text,
            {
                'domain_id': self.domain_id,
                'name': self.name
            }
        ).first()[0]


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.get_next_val = GetNextVal(self)
