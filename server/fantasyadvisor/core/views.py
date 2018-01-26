from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework import viewsets

from core.models import User
from core.serializers import UserSerializer, GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
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
