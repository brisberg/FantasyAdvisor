from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from yahoo import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
