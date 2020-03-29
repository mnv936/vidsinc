from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import vidapp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
     'websocket': AuthMiddlewareStack(
        URLRouter(
            vidapp.routing.websocket_urlpatterns
        )
    ),
})
