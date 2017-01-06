from django.conf.urls import url, include
from rest_framework import routers
from ScoopApp.views import CraftBeerAPIViewSet, VisitorAPIViewSet
from . import views
from ScoopApp.views import indexView


router = routers.DefaultRouter()
router.register(r'Craftbeers', CraftBeerAPIViewSet)
router.register(r'Visitors', VisitorAPIViewSet)


urlpatterns = [
    url(r'^$', views.indexView, name='indexView'),
    url(r'^map$', views.mapView, name='indexView'),
    url(r'^', include(router.urls)),
]