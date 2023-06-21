from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied


from .models import Blog
from .serializers import BlogSerializer
from accounts.permissions import IsAdmin, IsSupervisor, IsUser

from rest_framework.response import Response

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)

class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)

class BlogUpdateAPIView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated, IsSupervisor | IsAdmin)
    authentication_classes = (TokenAuthentication,)

    def handle_exception(self, exc):
        if isinstance(exc, AuthenticationFailed):
            return Response({'error': 'Authentication failed. Please provide a valid token.'}, status=401)
        elif isinstance(exc, PermissionDenied):
            return Response({'error': 'Permission denied. You do not have access to this resource.'}, status=403)
        return super().handle_exception(exc)

class BlogDestroyAPIView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdmin, IsAuthenticated)
    authentication_classes = (TokenAuthentication,)
    
    def handle_exception(self, exc):
        if isinstance(exc, AuthenticationFailed):
            return Response({'error': 'Authentication failed. Please provide a valid token.'}, status=401)
        elif isinstance(exc, PermissionDenied):
            return Response({'error': 'Permission denied. You do not have access to this resource.'}, status=403)
        return super().handle_exception(exc)