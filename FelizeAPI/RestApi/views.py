from .models import User, Client, Project, ProjectManager, ProjectResourceType, ProjectResource
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer, ProjectManagerSerializer, \
    ProjectResourceTypeSerializer, ProjectResourceSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectManagerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer


class ProjectResourceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = ProjectResourceType.objects.all()
    serializer_class = ProjectResourceTypeSerializer


class ProjectResourceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = ProjectResource.objects.all()
    serializer_class = ProjectResourceSerializer
