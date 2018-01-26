from rest_framework import serializers

from yahoo.models import League

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = League
        fields = ('url', 'id', 'title', 'game_code', 'owner')
