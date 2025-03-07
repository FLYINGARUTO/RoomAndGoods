from django.urls import path
from ..api_views.admin import *
urlpatterns = [
    path('api/post/user-list/',get_user_list),
    path('api/post/set-admin/',set_admin),
    path('api/post/del-user/',del_user)
] 