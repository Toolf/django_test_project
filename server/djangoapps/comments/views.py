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

from .models import Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, CommentDetailSerializer, CommentCreateSerializer, create_comment_serializer
from .paginations import (
    CommentLimitOffsetPagination,
    CommentPageNumberPagination
)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__username']
    pagination_class = CommentLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        return queryset_list


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = CommentCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        post_id = self.request.GET.get('post_id')
        parent_id = self.request.GET.get('parent_id', None)
        serializer = create_comment_serializer(
            model_type=model_type,
            post_id=post_id,
            parent_id=parent_id,
            user=self.request.user,
        )
        print(serializer)
        return serializer


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
