from django.urls import path
from ..api_views.notify import *

urlpatterns = [
    path('api/post/notify-list/',get_notify_lists),
    path('api/post/set-read/',read_notification)
]