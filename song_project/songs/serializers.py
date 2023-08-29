from rest_framework import serializers

from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'language', 'year', 'genre', 'slug')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'years', 'group')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'text', 'years', 'slug', 'album', 'group')
