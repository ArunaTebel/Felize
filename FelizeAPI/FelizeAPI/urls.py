from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include('RestApi.urls')),
]
