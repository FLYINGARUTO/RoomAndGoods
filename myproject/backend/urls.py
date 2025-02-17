from django.urls import path
from .api_urls.post import urlpatterns as post_urlpatterns
urlpatterns = []
urlpatterns.extend(post_urlpatterns)


