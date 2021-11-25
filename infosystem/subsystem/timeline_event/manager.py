import flask

from datetime import datetime
from infosystem.common import exception
from infosystem.common.subsystem import operation, manager
from infosystem.subsystem.timeline_event.resource \
    import TimelineEvent, TimelineEventUser


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


class GetAll(operation.List):

    def _get_timeline_event_from_user(self, session, user_id: str):
        timeline_events = session. \
            query(TimelineEvent). \
            join(TimelineEventUser,
                 TimelineEventUser.timeline_event_id == TimelineEvent.id). \
            filter(TimelineEventUser.user_id == user_id). \
            distinct(). \
            all()

        timeline_events = map(lambda e: e, timeline_events)
        return list(timeline_events)

    def pre(self, **kwargs):
        self.user_id = kwargs.get('user_id', None)
        if not self.user_id:
            raise exception.BadRequest('Erro! user_id is empty')
        return super().pre(**kwargs)

    def do(self, session, **kwargs):
        timeline_events = self._get_timeline_event_from_user(
            session, self.user_id)
        return timeline_events


class Manager(manager.Manager):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.create = Create(self)
        self.get_all = GetAll(self)
