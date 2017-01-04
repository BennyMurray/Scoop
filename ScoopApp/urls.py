from django.conf.urls import url, include
from rest_framework import routers
from ScoopApp.views import TestViewSet
from . import views
from ScoopApp.views import indexView


router = routers.DefaultRouter()
router.register(r'Craftbeers', TestViewSet)


urlpatterns = [
    url(r'^$', views.indexView, name='indexView'),
    url(r'^', include(router.urls)),
]