from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PROJECT_TYPE_CHOISES = (
    ("web", "تحت وب"),
    ("desktop", "دسکتاپ"),
    ("mobile", "موبایل"),
)

PROJECT_MEMBER_CHOISES = (
    (1, "یک"),
    (2, "دو"),
    (3, "سه"),
)


class Project(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=150, choices=PROJECT_TYPE_CHOISES)
    number_of_students = models.IntegerField(choices=PROJECT_MEMBER_CHOISES)
    description = models.TextField()
    is_suggested = models.BooleanField(default=False)

    def __str__(self):
        return self.title
