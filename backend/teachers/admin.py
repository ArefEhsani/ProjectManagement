from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ProjectReport)
admin.site.register(models.FinalReport)
admin.site.register(models.ProjectSetting)
admin.site.register(models.ReportParts)
