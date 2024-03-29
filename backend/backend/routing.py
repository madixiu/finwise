from websocket.consumers import *
from django.urls import re_path,path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
# from channels.sessions import SessionMiddlewareStack

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    # re_path(r"^messages/(?P<username>[\w.@+-]+)/$", firm_live), # noqa
                    # re_path(r"^ws/test$", optionData),
                    # re_path(r"^index_live/$", index_live),
                    re_path(r"^ws/random$", random),
                    re_path(r"^ws/marketwatch",MarketWatch),
                    re_path(r"^ws/Top5Views",Top5Viewed .as_asgi()),
                    re_path(r"^ws/ImpactOnIndex",getImpactOnIndex .as_asgi()),
                    re_path(r"^ws/HighestVolume",getHighestVolumes .as_asgi()),
                    re_path(r"^ws/HighestValues",getHighestValues .as_asgi()),
                    re_path(r"^ws/HighestSupplies",getHighestSupplies .as_asgi()),
                    re_path(r"^ws/HighestDemands",getHighestDemand .as_asgi()),

                ]
            )
        )
    )
})
