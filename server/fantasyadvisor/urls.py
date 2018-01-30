"""fantasyadvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.urls import path
from patches import routers
from core.urls import router as core_router
import core.views as views
from yahoo.urls import router as yahoo_router
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='FantasyAdvisor API')

router = routers.DefaultRouter()
router.extend(core_router)
router.extend(yahoo_router)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # social auth
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # end social auth
    url(r'^schema/$', schema_view),
    path('admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
