# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api import models, serializers, permissions


# POSTS SERIALIZER
class PostListAndCreate(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          permissions.IsOwnerOrReadOnly]


# COMMENTS SERIALIZER
class CommentListAndCreate(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          permissions.IsOwnerOrReadOnly]
