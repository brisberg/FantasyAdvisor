from django.contrib.auth.models import Group
from rest_framework import serializers

from core.models import User
from yahoo.models import League

class UserSerializer(serializers.HyperlinkedModelSerializer):
    leagues = serializers.PrimaryKeyRelatedField(many=True, queryset=League.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups', 'leagues', 'yahoo_auth_token')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = League
        fields = ('url', 'id', 'title', 'game_code', 'owner')
