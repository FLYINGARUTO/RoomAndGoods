from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from datetime import datetime,timezone
from django.utils.timesince import timesince

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
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'         
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__' 
class UserSerializer(serializers.ModelSerializer):
    unread_count=serializers.SerializerMethodField()#来自该用户的未读消息 仅在加载聊天列表时使用
    friendly_time=serializers.SerializerMethodField()#与该用户最后一次聊天的时间（友好格式） 仅在加载聊天列表时使用
    last_message=serializers.SerializerMethodField()#与该用户最后一次聊天的时间（标准格式） 仅在加载聊天列表时使用
    class Meta:
        model = User
        fields = ['id','username','is_staff','is_superuser','unread_count','last_message','friendly_time']  
    def get_unread_count(self,obj):
        user_id=self.context.get("user_id")
        return ChatMessage.objects.filter(sender=obj.id,receiver=user_id,is_read=0).count()
    def get_last_message(self, obj):
        user_id=self.context.get("user_id")
        chat_id=f"{min(user_id,obj.id)}_{max(user_id,obj.id)}"
        return ChatMessage.objects.filter(chat_id=chat_id).order_by("-create_at").first().create_at
    def get_friendly_time(self, obj):
        user_id=self.context.get("user_id")
        chat_id=f"{min(user_id,obj.id)}_{max(user_id,obj.id)}"
        now = datetime.now(timezone.utc)  # 获取当前时间（带时区）
        last_msg=ChatMessage.objects.filter(chat_id=chat_id).order_by("-create_at").first()
        delta = now - last_msg.create_at  # 计算时间差

        seconds = delta.total_seconds()
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        days = int(hours / 24)

        if minutes < 1:
            return "Just now"
        elif minutes < 60:
            return f"{minutes} mins"
        elif hours < 24:
            return f"{hours} hrs"
        elif days < 7:
            return f"{days} days"
        else:
            return last_msg.create_at.strftime("%Y-%m-%d %H:%M")  # 超过7天，显示标准时间