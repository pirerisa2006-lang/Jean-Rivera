from webbrowser import register

from django.contrib import admin
from .models import Project  #se carga o llama al modelo primero

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)