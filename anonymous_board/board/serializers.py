from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'create_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'create_date', 'post']
        read_only_fields = ['id', 'create_date', 'post']  # ✅ post는 자동 지정되니까 read_only로!


