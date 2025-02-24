from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes,permission_classes
from ..models import Banner,Post,PostPic
from rest_framework.permissions import IsAuthenticated
from ..serializer import *  # Import the serializer
from datetime import datetime
from ..utils.file import upload_to_s3
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

#获取所有帖子
@api_view(['GET'])
def get_post_list(request):
    posts = Post.objects.all()  # Get a single post
    for post in posts:
       post.create_time=post.create_time.strftime("%Y-%m-%d %H:%M:%S") 
    serialized_post = PostSerializer(posts,many=True)  # Convert to JSON format
    return Response({'code': 200, 'data': serialized_post.data})

#根据id获取帖子
@api_view(['GET'])
def get_post_by_id(request,id):

    post = Post.objects.get(id=id)  # Get a single post
    post.views+=1
    post.save()
    post.create_time=post.create_time.strftime("%Y-%m-%d %H:%M:%S")
    serialized_post = PostSerializer(post)  # Convert to JSON format
    return Response({'code': 200, 'data': serialized_post.data})

#获取帖子里的所有picture的urls
@api_view(['GET'])
def get_post_pic(request,id):
    pic_urls=PostPic.objects.filter(post=id)
    serialized_pics = PostPicSerializer(pic_urls,many=True)  # Convert to JSON format
    return Response({'code': 200, 'data': serialized_pics.data})

#获取帖子里的所有评论
@api_view(['GET'])
def get_comments(request,id):
    comments=Comment.objects.filter(post_id=id)
    for comment in comments:
        comment.create_time=comment.create_time.strftime("%Y-%m-%d %H:%M:%S")
    serialized_comments=CommentSerializer(comments,many=True)
    return Response({'code':200,'data':serialized_comments.data})

#发布评论
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def comment(request):
    print("request headers:",request.headers)
    comment = request.data.get('comment')
    from_id = request.data.get('from-id')
    to_id = request.data.get('to-id')
    post_id = request.data.get('post-id')
    commentObj=Comment.objects.create(from_id=from_id,to_id=to_id,post_id=post_id,comment=comment)
    commentObj.save()
    return Response({'code':200,'message':"Comment sent"})




"""
帖子发布
"""
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])  # Enables file uploads
def publish(request):

    #先创建post记录
    title=request.data.get('title')
    details=request.data.get('details')
    type=request.data.get('type')
    post=Post(publisher_id=1,title=title,details=details,category=type)
    post.save()
    #上传文件
    files=request.FILES.getlist('photos')
    saved_files=[]
    #遍历文件list
    for file in files:
        #上传到S3，并返回url
        url=upload_to_s3(file,settings.AWS_STORAGE_BUCKET_NAME)
        print(url)
        if url != '':
            saved_files.append(url)
            #创建帖子图片的数据库记录
            pic=PostPic.objects.create(post=post,photo_url=url)
            pic.save()
        else:
            print("something wrong with upload")
    return Response({'code':200,'urls':saved_files})

#点赞
@api_view(['post'])
@permission_classes([IsAuthenticated])
def like(request):
    userId=request.data.get('from-user')
    postOwnerId=request.data.get('to-id')
    postId=request.data.get('post-id')
    #创建Like记录
    like=Like.objects.create(from_user=userId,to_id=postOwnerId,post_id=postId)
    
    try:
        #Post记录点赞加1
        post=Post.objects.get(id=postId)
        post.likes+=1
        post.save()
        like.save()
        return Response({'code':200,'message':"'like' request has been handled"})
    except:
        return Response({'code':300,'message':"'like' request has failed"}) 
    



#取消点赞
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_like(request):
    userId=request.data.get('from-user')

    postId=request.data.get('post-id')
    #获取对应Like记录
    like=Like.objects.get(from_user=userId,post_id=postId)
    try:
        #修改Post记录 点赞-1
        post=Post.objects.get(id=postId)
        post.likes-=1
        post.save()
        like.delete()
        return Response({'code':200,'message':"'like' has been canceled"})
    except:
        return Response({'code':300,'message':"'like' request has failed"})  

#判断当前用户是否赞过某条帖子
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hasLiked(request):
    username=request.data.get('from-user')
    post_id=request.data.get('post-id')
    try:
        like=Like.objects.get(from_user=username,post_id=post_id)
        #print(like)
        return Response({'code':200,'data':{
            'message':"current user has liked this post",
            "code":1
        }})
    except:
       return Response({'code':200,'data':{
            'message':"current user has not liked this post",
            "code":0
        }}) 