from django.urls import re_path
from backend.consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_room>\w+)/$", ChatConsumer.as_asgi()),
]
