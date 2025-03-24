import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from ..serializer import *
from functools import wraps
from django.http import JsonResponse
from backend.models import Post


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
    users = User.objects.filter(is_staff=False).values("id", "username")  # ✅ 仅查询 `id` 和 `username`
    return Response({"code": 200, "data": list(users)})


#该请求需要superuser权限
#设置为普通管理员
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_admin(request):
    if not request.user.is_staff:  # ✅ 只有管理员可以设置其他用户为管理员
        return Response({"code": 403, "error": "权限不足，只有管理员可以执行此操作"}, status=403)

    user_id = request.data.get("user_id")
    if not user_id:
        return Response({"code": 400, "error": "缺少 user_id 参数"}, status=400)

    try:
        user = User.objects.get(id=user_id)
        if user.is_staff:
            return Response({"code": 400, "error": "该用户已经是管理员"}, status=400)

        user.is_staff = True
        user.save()
        return Response({"code": 200, "data":{"message": f"用户 {user.username} 已成为管理员"}})
    except User.DoesNotExist:
        return Response({"code": 404, "error": "用户不存在"}, status=404)

#删除用户
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@admin_required
def del_user(request):
    user_id = request.data.get("user_id")
    if not user_id:
        return Response({"code": 400, "error": "缺少 user_id 参数"}, status=400)

    try:
        user_to_delete = User.objects.get(id=user_id)

        if user_to_delete.is_staff:
            return Response({"code": 403, "error": "管理员不能删除其他管理员"}, status=403)

        user_to_delete.delete()
        return Response({"code": 200, "data":{"message": f"用户 {user_to_delete.username} 已被删除"}})

    except User.DoesNotExist:
        return Response({"code": 404, "error": "用户不存在"}, status=404)
    

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 先确保用户是认证的
def delete_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data.get("post_id")
            if not post_id:
                return JsonResponse({"code": 400, "message": "Post ID is required"}, status=400)

            post = Post.objects.filter(id=post_id).first()
            if not post:
                return JsonResponse({"code": 400, "message": "Post not found"}, status=404)

            # 这里可以加管理员权限验证
            post.delete()
            return JsonResponse({"code": 200, "message": "Post deleted successfully"})

        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e)}, status=500)

    return JsonResponse({"code": 405, "message": "Invalid request method"}, status=405)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
    comment_id = request.data.get("comment_id")
    if not comment_id:
        return JsonResponse({"code": 400, "message": "Comment ID is required"}, status=400)

    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({"code": 200, "message": "Comment deleted successfully"})
    except Comment.DoesNotExist:
        return JsonResponse({"code": 404, "message": "Comment not found"}, status=404)