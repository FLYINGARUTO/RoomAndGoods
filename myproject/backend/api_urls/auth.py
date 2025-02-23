from django.urls import path
from ..api_views.auth import *
urlpatterns = [
    path('api/post/register/',register) ,
    path('api/post/login/',user_login),
    path('api/get/logout',user_logout),
    path('api/post/token/refresh/',refresh_token)
] 