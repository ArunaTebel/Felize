from django.contrib import admin

from .models import Client, Project, ProjectManager, ProjectResourceType, ProjectResource

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(ProjectResourceType)
admin.site.register(ProjectResource)
