from django.urls import path
from .api_urls.post import urlpatterns as post_urlpatterns
from .api_urls.message import urlpatterns as message_urlpatterns
urlpatterns = []
urlpatterns.extend(post_urlpatterns)
urlpatterns.extend(message_urlpatterns)

