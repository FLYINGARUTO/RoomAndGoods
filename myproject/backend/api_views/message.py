from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..models import Message
from ..serializer import *  # Import the serializer
from datetime import datetime

@api_view(["POST"])
def send_msg(request):
    from_id=request.data.get('from-id') 
    to_id=request.data.get('to-id')
    msg=request.data.get('msg')
    message=Message.objects.create(from_id=from_id,to_id=to_id,text=msg)
    message.save()
    serilized = MessageSerializer(message)
    return Response({'code':200,'data':serilized.data})