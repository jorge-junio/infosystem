import json
import flask

from infosystem.common import exception
from infosystem.common.exception import BadRequest
from infosystem.common.subsystem import controller
from infosystem.database import db
from infosystem.subsystem.timeline_event.resource import TimelineEvent, TimelineEventUser


class Controller(controller.Controller):

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def _get_user_id_in_args(self):
        user_id = flask.request.args.get('user_id')
        if not user_id:
            raise BadRequest()
        return user_id

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

    def get_all(self):
        try:
            user_id = self._get_user_id_in_args()

            timeline_events = self._get_timeline_event_from_user(
                db.session, user_id)

            timeline_events_dict = self._entities_to_dict(
                timeline_events, self._get_include_dicts())
            response = {self.collection_wrap: timeline_events_dict}

            return flask.Response(response=json.dumps(response, default=str),
                                  status=200,
                                  mimetype="application/json")
        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)
