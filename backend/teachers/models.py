from django.db import models
from accounts.models import CollegeUsers
from administration.models import Project

# Create your models here.


class ProjectSetting(models.Model):
    can_get = models.BooleanField()
    suggest = models.BooleanField()
    reports = models.BooleanField()
    final_report = models.BooleanField()

    def __str__(self):
        return "برای تغییر ضربه بزنید"


class ReportParts(models.Model):
    report1 = models.BooleanField(default=True)
    report2 = models.BooleanField(default=False)
    report3 = models.BooleanField(default=False)
    report4 = models.BooleanField(default=False)
    report5 = models.BooleanField(default=False)
    report6 = models.BooleanField(default=False)
    report7 = models.BooleanField(default=False)
    report8 = models.BooleanField(default=False)

    def __str__(self):
        return "برای تغییر ضربه بزنید"


class ProjectReport(models.Model):
    student = models.ForeignKey(CollegeUsers, on_delete=models.CASCADE)
    number = models.IntegerField()
    file = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mark = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    is_submit = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} - {self.number}"


class FinalReport(models.Model):
    student = models.ForeignKey(CollegeUsers, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    file = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    mark = models.IntegerField(null=True, blank=True)
    is_archive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student}"
