from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from ..serializer import *
from functools import wraps
from django.http import JsonResponse 

def superuser_required(view_func):
    """ 自定义装饰器，返回 JSON 而不是 Django 默认的重定向 """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'code': 401, 'error': '未认证用户'}, status=401)
        if not request.user.is_superuser:
            return JsonResponse({'code': 403, 'error': '该请求需要superuser权限'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def admin_required(view_func):
    """ 自定义装饰器，返回 JSON 而不是 Django 默认的重定向 """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'code': 401, 'error': '未认证用户'}, status=401)
        if not request.user.is_staff:
            return JsonResponse({'code': 403, 'error': '该请求需要admin权限'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

#获取所有用户列表
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@admin_required
def get_user_list(request):
    users=User.objects.all()
    serialized=UserSerializer(users,many=True)
    return Response({'code':200,'data':serialized.data}) 


#该请求需要superuser权限
#设置为普通管理员
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@superuser_required
def set_admin(request):
    #获取需要修改权限的用户的id
    id=request.data.get('id')
    user=User.objects.get(id=id)
    if user:
        user.is_staff=True
        user.save()
        return Response({'code':200,'data':{'message':f"user(id:{id}) has been set as admin"}})
    return Response({'code':200,'data':{'message':f"user(id:{id}) does not exist"}})

#删除用户
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@admin_required
def del_user(request):
    """ 删除用户的 API """
    user_id = request.data.get('user_id')
    
    if not user_id:
        return Response({'code': 400, 'error': '缺少 user_id 参数'}, status=400)
    
    try:
        user_to_delete = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'code': 404, 'error': '用户不存在'}, status=404)

    # **权限判断逻辑**
    if request.user.is_superuser:
        # 超级用户可以删除任何用户
        user_to_delete.delete()
        return Response({'code': 200, 'data':{'message': f'用户 {user_to_delete.username} 已被删除'}}, status=200)
    
    if request.user.is_staff and not user_to_delete.is_staff:
        # 普通 staff 只能删除普通用户
        user_to_delete.delete()
        return Response({'code': 200, 'data':{'message': f'用户 {user_to_delete.username} 已被删除'}}, status=200)
    
    # 其他情况不允许删除
    return Response({'code': 403, 'error': '权限不足，无法删除该用户'}, status=403)
    

