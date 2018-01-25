from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from yahoo import views

urlpatterns = [
    url(r'^leagues/$', views.LeagueList.as_view()),
    url(r'^leagues/(?P<pk>[0-9]+)/$', views.LeagueDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
