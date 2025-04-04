from django.urls import path
from ..api_views.post import *

urlpatterns = [
    path('hello/', hello_world),
    path('test-post/',post_test),
    path('api/get/post_list/',get_post_list),

    path('api/get/post/<int:id>',get_post_by_id),
    path('api/get/pic-urls/<int:id>',get_post_pic),
    path('api/get/comments/<int:id>',get_comments),
    path('api/post/publish/',publish),
    path('api/post/comment/',comment),
    path('api/post/like/',like),
    path('api/post/cancel-like/',cancel_like),
    path('api/post/like-or-not/',hasLiked),
    path('api/post/star/',star),
    path('api/post/cancel-star/',cancel_star),
    path('api/post/star-or-not/',hasStarred),
    path('api/post/notify-test/',notify_test)
     
    
]
