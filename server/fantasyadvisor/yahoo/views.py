from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from yahoo.serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse, JsonResponse
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

@csrf_exempt
def league_list(request):
    """
    List all leagues, or create a new league.
    """
    if request.method == 'GET':
        leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LeagueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def league_detail(request, pk):
    """
    Retrieve, update or delete a league.
    """
    try:
        league = League.objects.get(pk=pk)
    except League.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LeagueSerializer(league)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LeagueSerializer(league, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        league.delete()
        return HttpResponse(status=204)
