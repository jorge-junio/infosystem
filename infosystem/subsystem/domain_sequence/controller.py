import flask

from infosystem.common import exception, utils
from infosystem.common.subsystem import controller


class Controller(controller.Controller):

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def get_next_val(self, id):
        data = flask.request.get_json()

        try:
            if 'name' not in data:
                raise exception.BadRequest(
                    'ERRO! "name" não foi enviado na requisição')

            response = self.manager.get_next_val(
                id=id,
                name=data['name'])
        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response = {'next_val': response}

        return flask.Response(response=utils.to_json(response),
                              status=200,
                              mimetype="application/json")
