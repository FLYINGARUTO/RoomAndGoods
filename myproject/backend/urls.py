from django.urls import path
from .views import *
urlpatterns = [
    path('hello/', hello_world),
    path('test-post/',post_test),
    path('get_post_list/',get_post_list)
]
