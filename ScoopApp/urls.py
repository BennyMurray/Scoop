from django.conf.urls import url
from rest_framework import routers
from ScoopApp.views import TestViewSet

router = routers.DefaultRouter()
router.register(r'Craftbeers', TestViewSet)


urlpatterns = router.urls