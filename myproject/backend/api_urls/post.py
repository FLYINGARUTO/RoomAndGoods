from django.urls import path
from ..api_views.post import *

urlpatterns = [
    path('hello/', hello_world),
    path('test-post/',post_test),
    path('api/get/post-list/',get_post_list),
    path('api/get/post/<int:id>',get_post_by_id),
    path('api/get/pic-urls/<int:id>',get_post_pic),
    path('api/get/comments/<int:id>',get_comments),
    path('api/post/publish/',publish)
]
