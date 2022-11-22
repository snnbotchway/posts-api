from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    '''ViewSet to add a customer'''
    serializer_class = PostSerializer
    queryset = Post.objects.all()
