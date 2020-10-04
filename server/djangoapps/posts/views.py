from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostDeleteSerializer,
)
from .paginations import (
    PostLimitOffsetPagination,
    PostPageNumberPagination
)

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'created_at']
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(created_at__icontains=query) |
                Q(owner__username__icontains=query)
            ).distinct()
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


# class CommentCreateAPIView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentCreateSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
