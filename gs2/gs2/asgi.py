import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import app.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs2.settings")

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(
        app.routing.websocket_urlpatterns
    )
})

# application = get_asgi_application()
