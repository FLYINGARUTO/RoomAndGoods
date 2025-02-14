from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Banner,Post,PostPic
from .serializer import PostSerializer  # Import the serializer

@api_view(['GET'])
def hello_world(request):
    # banner=Banner.objects.create(picture_url="/static/pic/1.png",admin_id=10)
    # banner.save()
    
    return Response({"message": "Hello from Django!"})


#发布帖子的测试
@api_view(['GET'])
def post_test(request):
    post = Post.objects.create(publisher_id=3,title='post-test',
                               details='post-test',category='sublet')
    postpic1=PostPic.objects.create(post=post,photo_url='11.txt',order=1)
    postpic2=PostPic.objects.create(post=post,photo_url='12.txt',order=2) 
    post.save()
    postpic1.save()
    postpic2.save()
    return Response({'code':200,'message':"success"})

@api_view(['GET'])
def get_post_list(request):
    post = Post.objects.all()  # Get a single post
    serialized_post = PostSerializer(post,many=True)  # Convert to JSON format
    return Response({'code': 200, 'data': serialized_post.data})