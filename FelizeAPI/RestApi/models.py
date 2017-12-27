from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'felize_client'


class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'felize_project'


class ProjectManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '[PM] ' + self.user.first_name + ' ' + self.user.last_name + ' [' + self.project.name + ']'

    class Meta:
        db_table = 'felize_project_manager'


class ProjectResourceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'felize_project_resource_type'


class ProjectResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource_type = models.ForeignKey(ProjectResourceType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '[PR : ' + self.resource_type.name + ' | ' + self.project.name + '] ' + self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = 'felize_project_resource'
