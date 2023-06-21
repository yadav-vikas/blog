from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_by','updated_by', 'created_at', 'updated_at')