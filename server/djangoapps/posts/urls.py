from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostCreateAPIView,
    PostDeleteAPIView,
)


urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]
