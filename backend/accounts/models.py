from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CollegeUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
