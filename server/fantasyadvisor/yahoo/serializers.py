from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yahoo.models import League

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class LeagueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    game_code = serializers.CharField(max_length=10)

    def create(self, validated_data):
        """
        Create and return a new `League` instance, given the validated data.
        """
        return League.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `League` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.game_code = validated_data.get('game_code', instance.game_code)
        instance.save()
        return instance
