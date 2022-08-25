from django.db import models

# Create your models here.


class ProjectSetting(models.Model):
    can_get = models.BooleanField()
    suggest = models.BooleanField()
    reports = models.BooleanField()
    final_report = models.BooleanField()

    def __str__(self):
        return "برای تغییر ضربه بزنید"
