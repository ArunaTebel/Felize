from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'project_managers', views.ProjectManagerViewSet)
router.register(r'project_resource_types', views.ProjectResourceTypeViewSet)
router.register(r'project_resources', views.ProjectResourceViewSet)

urlpatterns = [
    url(r'^felize/', include(router.urls)),
]