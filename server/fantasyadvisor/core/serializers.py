from django.contrib.auth.models import User, Group
from social_django.models import UserSocialAuth
from rest_framework import serializers

# from core.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    social_auth = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='provider'
     )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups', 'social_auth')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
