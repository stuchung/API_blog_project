from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

# Create your views here.
"""
The below was original four views
"""

# class PostList(generics.ListCreateAPIView):
#     """Django REST ListCreateAPIView for data model Post"""
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     #permission_classes = (permissions.IsAuthenticated,)
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     """Django REST RetrieveUpdateDestroyAPIView for data model NAME"""
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


"""This is the updated view wich uses viewsets instead
  to reduce coding. Same view only i had to define the
  queryset and serializers once for each view above
"""
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
