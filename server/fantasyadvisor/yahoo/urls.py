from django.conf.urls import url
from yahoo import views

urlpatterns = [
    url(r'^leagues/$', views.league_list),
    url(r'^leagues/(?P<pk>[0-9]+)/$', views.league_detail),
]
