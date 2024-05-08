from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:groupkanaam>/',consumers.Myconsumer.as_asgi()),
]