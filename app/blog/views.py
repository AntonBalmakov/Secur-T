from rest_framework import generics, permissions
from .models import Post
from .models import Comment
from .serializers import PostListSerializers
from .serializers import PostDetailSerializers
from .serializers import CommentCreateSerializers


class PostListView(generics.ListAPIView, generics.CreateAPIView):
    """Вывод списка постов"""

    serializer_class = PostListSerializers
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class PostDetailView(generics.RetrieveAPIView, generics.DestroyAPIView):
    """Вывод поста"""

    serializer_class = PostDetailSerializers
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class CommentCreateView(generics.UpdateAPIView, generics.CreateAPIView):
    """Добавление коментария к посту"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers
    permission_classes = [permissions.AllowAny]


class CommentDeleteView(generics.RetrieveAPIView, generics.DestroyAPIView):
    """Удаление коментария к посту"""
    queryset = Comment
    serializer_class = CommentCreateSerializers
    permission_classes = [permissions.AllowAny]


