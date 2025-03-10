from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken
from ..serializer import *



def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }
@api_view(['post'])
def register(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return Response({'code':200,'message':"successfully registered"})

@csrf_exempt  # 禁用 CSRF 检查
@api_view(['post'])
def user_login(request):
    username=request.data.get('username')
    password=request.data.get('password') 
    user=authenticate(request,username=username,password=password)
    if user is not None:
        tokens = get_token_for_user(user)
        return Response({'code':200,'message':"Successfully Logged in",'data':{'token':tokens,'loginedUser':username,'userId':user.id}})
    else:
        return Response({'code':302,'message':"Failed to Log in"}) 
    
@api_view(['get'])
def user_logout(request):
    logout(request)
    return Response({'code':200,'message':"Successfully logged out"})

# ✅ 手动刷新 Token 接口（也可以直接用 `SimpleJWT` 自带的视图）
@api_view(['POST'])
def refresh_token(request):
    refresh = request.data.get("refresh")  # 获取 `refreshToken`
    if not refresh:
        return Response({"error": "Refresh token is required"}, status=400)

    from rest_framework_simplejwt.tokens import RefreshToken
    try:
        new_token = RefreshToken(refresh).access_token  # 生成新的 `accessToken`
        return Response({"access": str(new_token)})
    except Exception as e:
        return Response({"error": "Invalid refresh token"}, status=400)
