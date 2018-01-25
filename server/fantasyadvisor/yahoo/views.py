from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics

from yahoo.models import League
from yahoo.serializers import UserSerializer, GroupSerializer, LeagueSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
