from django.urls import path
from . import views

urlpatterns = [
    path('teachers-list', views.teachers_list, name="teachers_list"),
    path('teachers-list/delete/<id>', views.delete_teacher, name="delete_teacher"),
    path('students-list', views.students_list, name="students_list"),
    path('students-list/delete/<id>', views.delete_student, name="delete_student"),
    path('projects-list', views.projects_list, name="projects_list"),
]
