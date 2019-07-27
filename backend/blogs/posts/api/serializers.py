from rest_framework import serializers
from posts.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'image',
        )