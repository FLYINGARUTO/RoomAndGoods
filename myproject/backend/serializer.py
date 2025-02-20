from rest_framework import serializers
from .models import *
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # or specify only needed fields, e.g., ['id', 'title', 'content']
class PostPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPic
        fields = '__all__'  # or specify only needed fields, e.g., ['id', 'title', 'content']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # or specify only needed fields, e.g., ['id', 'title', 'content']
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  # or specify only needed fields, e.g., ['id', 'title', 'content']