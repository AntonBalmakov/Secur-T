from rest_framework import serializers
from .models import Post
from .models import Comment


class PostListSerializers(serializers.ModelSerializer):
    """Список постов"""

    class Meta:
        model = Post
        fields = ('id', 'title', 'content')


class FilterCommentsListserializer(serializers.ListSerializer):
    """Фильтр комментариев, только родители"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentCreateSerializers(serializers.ModelSerializer):
    """Создание коментариев"""

    class Meta:
        model = Comment
        fields = '__all__'


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекоурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializers(serializers.ModelSerializer):
    """Выовд Комментариев"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_seralizer_class = FilterCommentsListserializer
        model = Comment
        fields = ('name', 'body', 'children')


class PostDetailSerializers(serializers.ModelSerializer):
    """Описание поста"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comment = CommentSerializers(many=True)

    class Meta:
        model = Post
        fields = '__all__'
