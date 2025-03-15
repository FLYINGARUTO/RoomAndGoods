from django.urls import path
from .api_urls.post import urlpatterns as post_urlpatterns
from .api_urls.message import urlpatterns as message_urlpatterns
from .api_urls.auth import urlpatterns as auth_urlpatterns
from .api_urls.my import urlpatterns as my_urlpatterns
from .api_urls.admin import urlpatterns as admin_urlpatterns
from .api_urls.notify import urlpatterns as notify_urlpatterns
urlpatterns = []
urlpatterns.extend(post_urlpatterns)
urlpatterns.extend(message_urlpatterns)
urlpatterns.extend(auth_urlpatterns)
urlpatterns.extend(my_urlpatterns)
urlpatterns.extend(admin_urlpatterns)
urlpatterns.extend(notify_urlpatterns)
