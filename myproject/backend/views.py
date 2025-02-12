from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Banner

@api_view(['GET'])
def hello_world(request):
    banner=Banner.objects.create(picture_url="/static/pic/1.png",admin_id=10)
    banner.save()
    return Response({"message": "Hello from Django!"})
