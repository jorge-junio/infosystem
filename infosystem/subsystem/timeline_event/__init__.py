from infosystem.common import subsystem
from infosystem.subsystem.timeline_event \
    import resource, router, controller, manager


subsystem = subsystem.Subsystem(resource=resource.TimelineEvent,
                                router=router.Router,
                                controller=controller.Controller,
                                manager=manager.Manager)
