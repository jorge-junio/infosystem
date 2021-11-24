import json
import flask

from infosystem.common import exception
from infosystem.common.exception import BadRequest
from infosystem.common.subsystem import controller


class Controller(controller.Controller):

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def _get_user_id_in_args(self):
        user_id = flask.request.args.get('user_id')
        if not user_id:
            raise BadRequest()
        return user_id

    def get_all(self):
        # TODO()
        try:
            user_id = self._get_user_id_in_args()

            timeline_events = self.manager.list(owner_id=user_id)

            timeline_events_dict = self._entities_to_dict(
                timeline_events, self._get_include_dicts())
            response = {self.collection_wrap: timeline_events_dict}

            return flask.Response(response=json.dumps(response, default=str),
                                  status=200,
                                  mimetype="application/json")
        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)
