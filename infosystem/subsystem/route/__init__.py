from infosystem.common import subsystem
from infosystem.subsystem.route import resource, manager, controller, router


subsystem = subsystem.Subsystem(resource=resource.Route,
                                manager=manager.Manager,
                                controller=controller.Controller,
                                router=router.Router)
