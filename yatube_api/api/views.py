# TODO:  Напишите свой вариант
from rest_framework import viewsets
# from rest_framework import permissions
from posts.models import Post, Comment, Group, Follow
# from yatube_api.posts.models import Group
from .serializers import PostSerializer, CommentSerializer, GroupSerializer
from .serializers import FollowSerializer
# from rest_framework.views import PermissionDenied
# vfrom rest_framework.pagination import PageNumberPagination
from .permissions import ReadOnlyPermission
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, status, viewsets
from rest_framework.pagination import LimitOffsetPagination


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (ReadOnlyPermission,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (ReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (ReadOnlyPermission,)
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset


class FollowViewSet(CreateListViewSet):
    filter_backends = (filters.SearchFilter,)
    serializer_class = FollowSerializer
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
