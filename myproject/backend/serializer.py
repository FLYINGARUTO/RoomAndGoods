from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField() #添加自定义字段
    class Meta:
        model = Post
        fields = '__all__'  # or specify only needed fields, e.g., ['id', 'title', 'content']
    def get_image(self,obj):
        postPic=PostPic.objects.filter(post=obj).first()
        return postPic.photo_url if postPic else None #防止NoneType错误
        
class PostPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPic
        fields = '__all__'  
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__' 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','is_staff','is_superuser']  