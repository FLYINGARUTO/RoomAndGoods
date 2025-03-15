
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializer import *  # Import the serializer




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_notify_lists(request):
    user_id=request.user.id
    print(user_id)
    notifications=Notification.objects.filter(user_id=user_id)
    serialized = NotificationSerializer(notifications,many=True)
    return Response({"code":200,"data":serialized.data})
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def read_notification(request):
    notify_id=request.data.get("notify-id")

    try:
        notification=Notification.objects.get(id=notify_id)
        notification.is_read=1
        notification.save()
        return Response({"code":200,"message":f"notification (id:{notify_id}) set as read"})
    except Exception as e:
        import traceback
        error_message = traceback.format_exc()  # 获取完整的错误堆栈信息
        print(error_message)  # 直接在后端终端输出
        return Response({'code': 500, 'message': 'Internal server error', 'error': str(e), 'traceback': error_message})
         
    
