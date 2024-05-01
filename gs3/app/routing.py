from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/asc/',consumers.Myasyncconsumer.as_asgi()),
]