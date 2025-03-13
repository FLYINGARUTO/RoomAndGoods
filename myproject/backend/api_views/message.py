from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes,permission_classes
# from ..models import Message
from ..serializer import *  # Import the serializer
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def send_msg(request):
#     from_user=request.data.get('from-user') 
#     to_user=request.data.get('to-user')
#     msg=request.data.get('msg')
#     message=Message.objects.create(from_user=from_user,to_user=to_user,text=msg)
#     message.save()
#     serilized = MessageSerializer(message)
#     return Response({'code':200,'data':serilized.data})

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def get_msg_lists(request):
#     username=request.data.get("username")
#     messages=Message.objects.filter(to_user=username)
#     for msg in messages:
#         msg.created_time=msg.created_time.strftime("%Y-%m-%d %H:%M:%S")
#     serilized = MessageSerializer(messages,many=True)
#     return Response({'code':200,'data':serilized.data}) 

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def unread_amount(request):
#     username=request.data.get("username") 
#     messages=Message.objects.filter(to_user=username,read=0)  
#     return Response({'code':200,'data':len(messages)}) 

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def read(request):
#     id=request.data.get('id')
#     message=Message.objects.get(id=id)
#     message.read=1
#     message.save()
#     return Response({'code':200,'data':f"message(id:{id}) has been read"})  

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def readAll(request):
#     username=request.data.get('username')
#     messages=Message.objects.filter(to_user=username)
#     for msg in messages:
#         msg.read=1
#         msg.save()
#     return Response({'code':200,'data':f"{username}'s message box has all been marked as read"})  

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def reply(request):
#     id=request.data.get('id') #the id of the msg that's being replied
#     message=Message.objects.get(id=id) 
#     message.read=1
#     message.reply=1#change the status
#     message.save()
#     #creating a new message record
#     fromUser=request.data.get('from-user') 
#     toUser=request.data.get('to-user')
#     msg=request.data.get('msg') 
#     replyMsg=Message.objects.create(from_user=fromUser,to_user=toUser,text=msg)
#     replyMsg.save()
#     return Response({'code':200,'data':f"reply to message(id:{id}) has been made"})





#获取与某个用户的聊天记录
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_chat_messages(request):
    user=request.user.id #当前登录用户
    chatWith=int(request.data.get('chatWith') ) #聊天对象
    chatId=f"{min(user,chatWith)}_{max(user,chatWith)}" #当前对话的id
    messages=ChatMessage.objects.filter(chat_id=chatId)
    for msg in messages:
        msg.is_read=1#标记为已读
        msg.save()
    serialized=ChatMessageSerializer(messages,many=True)
    return Response({'code':200,'data':serialized.data})

#获取当前登录用户的聊天列表

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_chat_list(request):
    user_id=request.user.id #当前登录用户
    
    if not user_id:
        return Response({"error": "user_id is required"}, status=400)
    #获取与当前登录用户有关聊天记录里的所有sender id、receiver id
    chat_users=ChatMessage.objects.filter(
        Q(sender_id=user_id)|Q(receiver_id=user_id)
        ).values_list('sender','receiver')
    #去重复
    #排除当前登录用户
    chat_users_set=set()
    for sender,receiver in chat_users:
        if sender!=user_id:
            chat_users_set.add(sender)
        if receiver!=user_id:
            chat_users_set.add(receiver)
    #根据id获取用户信息
    users=User.objects.filter(id__in = chat_users_set)
    serialized = UserSerializer(users,many=True,context={'user_id':user_id})
    return Response({'code':200,'data':serialized.data})