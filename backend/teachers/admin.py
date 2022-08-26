from django.contrib import admin
from . import models
# Register your models here.


class ReportPartsAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active')


admin.site.register(models.ProjectReport)
admin.site.register(models.FinalReport)
admin.site.register(models.ProjectSetting)
admin.site.register(models.ReportParts, ReportPartsAdmin)
