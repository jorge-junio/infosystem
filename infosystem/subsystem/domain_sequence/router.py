from infosystem.common.subsystem import router


class Router(router.Router):

    def __init__(self, collection, routes=[]):
        super().__init__(collection, routes)

    @property
    def routes(self):
        return super().routes + [
            {
                'action': 'Obter novo valor da sequência',
                'method': 'PUT',
                'url': self.resource_url + '/next_val',
                'callback': 'get_next_val',
            }]
