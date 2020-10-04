from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    CommentDeleteAPIView,
)


app_name = 'posts'
urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='detail'),
    # path('<int:pk>/delete/', CommentDeleteAPIView.as_view(), name='delete'),
]
