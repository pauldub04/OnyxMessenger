from rest_framework import serializers
from .models import Post, Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'owner', 'theme', 'created', 'icon']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'annotation', 'creator_channel', 'icon', 'body']
