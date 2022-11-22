"""Serializers for the post API"""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post model serializer"""

    class Meta:
        model = Post
        fields = ["id", "title",
                  "content", "created_at", "last_updated"]
