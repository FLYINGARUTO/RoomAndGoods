from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes,permission_classes
from ..models import Banner,Post,PostPic
from rest_framework.permissions import IsAuthenticated
from ..serializer import *  # Import the serializer
from datetime import datetime


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_liked_post(request):
    username=request.data.get('username')
    postIds=Like.objects.filter(from_user=username).values_list('post_id',flat=True) #获取到用户所有赞过的帖子的id
    posts=Post.objects.filter(id__in=postIds)
    for post in posts:
       post.create_time=post.create_time.strftime("%Y-%m-%d %H:%M:%S")
    serilized=PostSerializer(posts,many=True)
    return Response({'code':200,'data':serilized.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_starred_post(request):
    username=request.data.get('username')
    postIds=Collect.objects.filter(from_user=username).values_list('post_id',flat=True) #获取到用户所有收藏过的帖子的id
    posts=Post.objects.filter(id__in=postIds)
    for post in posts:
       post.create_time=post.create_time.strftime("%Y-%m-%d %H:%M:%S") 
    serilized=PostSerializer(posts,many=True)
    return Response({'code':200,'data':serilized.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_my_posts(request):
    username=request.data.get('username')
    posts=Post.objects.filter(publisher=username)
    for post in posts:
       post.create_time=post.create_time.strftime("%Y-%m-%d %H:%M:%S")
    serilized=PostSerializer(posts,many=True) 
    return Response({'code':200,'data':serilized.data}) 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_post(request):
    postId=request.data.get('post-id')
    post=Post.objects.get(id=postId)
    if post is not None:
        post.delete()
        return Response({'code':200,'data':{'message':"post is deleted"}})  
    return Response({'code':200,'data':{'message':"something went wrong"}})   