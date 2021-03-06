from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework import serializers

from .models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username',)
        read_only_fields = ('id', 'username',)


def create_comment_serializer(model_type='post', post_id=None, parent_id=None, user=None):
    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'id',
                'parent',
                'content',
                'timestamp',
            ]

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.post_id = post_id
            self.parent_obj = None
            print(self.__dict__)
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    self.parent_obj = parent_qs.first()
            super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            print("data: ", data)
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError('This is not a valid content type')
            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(pk=post_id)
            print(obj_qs.exists(), obj_qs.count())
            if not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError('This is not a post_id for this content type')
            return data

        def create(self, validated_data):
            content = validated_data.get('content')
            if user:
                main_user = user
            else:
                raise Exception("Who are you")
            model_type = self.model_type
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                model_type=model_type,
                post_id=post_id,
                content=content,
                user=user,
                parent_obj=parent_obj
            )
            return comment

    return CommentCreateSerializer


class CommentSerializer(serializers.ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
            'reply_count'
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp'
        ]


class CommentDetailSerializer(serializers.ModelSerializer):
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'replies',
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'content_type',
            'object_id',
        ]
