from django.contrib import admin
from . import models
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "type", "number_of_students")


admin.site.register(models.Project, ProjectAdmin)
