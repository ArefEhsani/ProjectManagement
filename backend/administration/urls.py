from django.urls import path
from . import views

urlpatterns = [
    path('teachers-list', views.teachers_list, name="a_teachers_list"),
    path('teachers-list/delete/<id>', views.delete_teacher, name="a_delete_teacher"),
    path('students-list', views.students_list, name="a_students_list"),
    path('students-list/delete/<id>', views.delete_student, name="a_delete_student"),
    path('projects-list', views.projects_list, name="a_projects_list"),
]
