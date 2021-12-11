from django.contrib.auth.models import User
from rest_framework import serializers
from movies_web.models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'description', 'premiere']
