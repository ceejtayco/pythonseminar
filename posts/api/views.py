from rest_framework import viewsets
from .serializers import BlogSerializer
from posts.models import Blog

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

