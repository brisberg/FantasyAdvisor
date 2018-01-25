from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yahoo.serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from yahoo.models import League
from yahoo.serializers import LeagueSerializer


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

@api_view(['GET', 'POST'])
def league_list(request, format=None):
    """
    List all leagues, or create a new league.
    """
    if request.method == 'GET':
        leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def league_detail(request, pk, format=None):
    """
    Retrieve, update or delete a league.
    """
    try:
        league = League.objects.get(pk=pk)
    except League.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeagueSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeagueSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        league.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
