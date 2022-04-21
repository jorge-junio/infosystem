import flask
from infosystem.common.subsystem import controller
from infosystem.common import exception, utils


class Controller(controller.Controller):

    def tests(self):
        try:
            users = self.manager.tests()
            response = {'users': self._entities_to_dict(users)}

            return flask.Response(response=utils.to_json(response),
                                status=200,
                                mimetype="application/json")

        except exception.InfoSystemException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)
