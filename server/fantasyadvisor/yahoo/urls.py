from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from yahoo import views

urlpatterns = [
    url(r'^leagues/$', views.league_list),
    url(r'^leagues/(?P<pk>[0-9]+)/$', views.league_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
