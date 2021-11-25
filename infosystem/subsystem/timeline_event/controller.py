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

    def _get_user_from_token(self):
        if flask.has_request_context():
            token_id = flask.request.headers.get('token')
            if token_id is not None:
                self.token = self.manager.api.tokens().get(id=token_id)
                return self.token.user_id
        return None

    def get_all(self):
        try:
            # user_id = self._get_user_id_in_args()
            user_id = self._get_user_from_token()

            if user_id is not None:
                timeline_events = self.manager.get_all(user_id=user_id)
            else:
                return flask.Response("Não encontrou user_id",
                                      status=404)

            timeline_events_dict = self._entities_to_dict(
                timeline_events, self._get_include_dicts())
            response = {self.collection_wrap: timeline_events_dict}

            return flask.Response(response=json.dumps(response, default=str),
                                  status=200,
                                  mimetype="application/json")
        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)
