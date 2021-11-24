import flask

from datetime import datetime
from infosystem.common import exception
from infosystem.common.subsystem import operation, manager


class Create(operation.Create):

    def pre(self, session, **kwargs):
        kwargs['lat'] = kwargs.get('lat', '0')
        kwargs['lon'] = kwargs.get('lon', '0')
        kwargs['event_at'] = kwargs.get('event_at', datetime.now())

        if 'event_by' not in kwargs:
            if flask.has_request_context():
                token_id = flask.request.headers.get('token')
                if token_id is not None:
                    self.token = self.manager.api.tokens().get(id=token_id)
                    kwargs['event_by'] = self.token.user_id
            else:
                kwargs['event_by'] = 'integracao'
        return super().pre(session, **kwargs)


class Manager(manager.Manager):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.create = Create(self)
