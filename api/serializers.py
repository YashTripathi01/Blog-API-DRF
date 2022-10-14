from rest_framework import serializers

from api import models


# POSTS SERIALIZER
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'body', 'owner', 'comments']


# COMMENTS SERIALIZER
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = models.Comment
        fields = ['id', 'body', 'owner', 'post']
