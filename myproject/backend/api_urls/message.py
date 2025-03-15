from django.urls import path
from ..api_views.message import *


urlpatterns = [
    # path('api/post/send-msg/',send_msg),
    # path('api/post/msg-list/',get_msg_lists),
    # path('api/post/unread-num/',unread_amount),
    # path('api/post/read/',read),
    # path('api/post/read-all/',readAll),
    # path('api/post/reply/',reply),
    path('api/post/load-chat/',get_chat_messages),
    path('api/post/chat-list/',get_chat_list)

]