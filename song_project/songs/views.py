from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response


from .serializers import *


class GroupAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupAPIPutView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AlbumAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumApiPutView(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
