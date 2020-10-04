from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from .models import Post, User
from comments.serializers import CommentSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)
        read_only_fields = ('id', 'username',)


class PostListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    comments = CommentSerializer(many=True)
    url = HyperlinkedIdentityField(
        view_name='posts:detail',
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'owner',
            'created_at',
            'comments',
            'url'
        )
        read_only_fields = ('id', 'owner', 'created_at', 'comments')


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'comments')
        read_only_fields = ('id', 'title' 'owner', 'create_at', 'content')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')


class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'comments')
        read_only_fields = ('id', 'title' 'owner', 'create_at', 'content')
