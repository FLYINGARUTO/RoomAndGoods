from django.urls import path
from ..api_views.message import *


urlpatterns = [
    path('api/post/send-msg/',send_msg)
]