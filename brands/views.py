# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brands.models import Info
from brands.permissions import IsOwnerOrReadOnly
from brands.serializers import InfoSerializer, UserSerializer



class InfoList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)

    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                            IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication,)

    queryset = Info.objects.all()
    serializer_class = InfoSerializer




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
