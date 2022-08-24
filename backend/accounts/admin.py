from django.contrib import admin
from . import models


class CollegeUsersAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "is_teacher", "is_student")


admin.site.register(models.CollegeUsers, CollegeUsersAdmin)
