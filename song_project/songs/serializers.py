from rest_framework import serializers

from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'language', 'year', 'genre', 'slug')

