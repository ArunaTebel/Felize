from .models import User, Client, Project, ProjectManager, ProjectResourceType, ProjectResource
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('url', 'name', 'description')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'client', 'name', 'description', 'start_date', 'end_date')


class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = ('url', 'user', 'project')


class ProjectResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectResourceType
        fields = ('url', 'name')


class ProjectResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectResource
        fields = ('url', 'user', 'project')
