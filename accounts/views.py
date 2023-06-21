from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    authentication_classes = (TokenAuthentication,)

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    authentication_classes = (TokenAuthentication,)