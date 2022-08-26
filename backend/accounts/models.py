from django.db import models
from django.contrib.auth.models import User
from administration.models import Project

# Create your models here.


class CollegeUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    project = models.ForeignKey(Project, models.SET_NULL, null=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
