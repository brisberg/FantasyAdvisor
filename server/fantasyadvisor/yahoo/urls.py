from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from yahoo import views

from yahoo.views import LeagueViewSet, UserViewSet, GroupViewSet, api_root

league_list = LeagueViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
league_detail = LeagueViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
group_list = GroupViewSet.as_view({
    'get': 'list'
})
group_detail = GroupViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^leagues/$', league_list, name='league-list'),
    url(r'^leagues/(?P<pk>[0-9]+)/$', league_detail, name='league-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^groups/$', group_list, name='group-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$', group_detail, name='group-detail'),
])
