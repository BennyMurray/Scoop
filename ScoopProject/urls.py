from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('ScoopApp.urls', namespace='ScoopApp')),
    url(r'', include('ScoopApp.urls')),
    url(r'^map', include('ScoopApp.urls')),
    url(r'^about', include('ScoopApp.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

