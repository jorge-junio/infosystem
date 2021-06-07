from infosystem.common.subsystem.controller import Controller
from infosystem.common import subsystem
from infosystem.subsystem.domain_sequence \
    import resource, controller, manager, router


subsystem = subsystem.Subsystem(resource=resource.DomainSequence,
                                controller=controller.Controller,
                                manager=manager.Manager,
                                router=router.Router)
