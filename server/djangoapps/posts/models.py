from django.contrib.auth import get_user_model
from django.db import models

from comments.models import Comment

User = get_user_model()

class PostManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at")


class Post(models.Model):
    objects = PostManager()

    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def comments(self):
        queryset = Comment.objects.filter_by_instance(self)
        return queryset
