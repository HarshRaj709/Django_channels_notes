import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from app import routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs4.settings")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':URLRouter(
        routing.websocket_urlpatterns
    )
})

#application = get_asgi_application()
