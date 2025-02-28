from django.urls import path
from ..api_views.my import *


urlpatterns = [
    path('api/post/get-liked-posts/',get_liked_post),
    path('api/post/get-starred-posts/',get_starred_post),
    path('api/post/get-my-posts/',get_my_posts)
]