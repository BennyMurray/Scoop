from django.conf.urls import url, include
from rest_framework import routers
from ScoopApp.views import CraftBeerAPIViewSet, VisitorAPIViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'Craftbeers', CraftBeerAPIViewSet)
router.register(r'Visitors', VisitorAPIViewSet)


urlpatterns = [
    url(r'^$', views.indexView, name='indexView'),
    url(r'^map$', views.mapView, name='mapView'),
    url(r'about', views.aboutView, name='aboutView'),
    url(r'^', include(router.urls)),
]