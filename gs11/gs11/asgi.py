import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gs11.settings")
from channels.routing import ProtocolTypeRouter,URLRouter
from app import routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        routing.websocket_urlpatterns
    )
})

#application = 
