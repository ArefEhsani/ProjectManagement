from django.urls import path
from . import views
urlpatterns = [
    path('student-permissions', views.student_permissions, name="t_student_permissions"),
    path('create-project', views.create_project, name="t_create_project"),
    path('projects-list', views.projects_list, name="t_projects_list"),
    path('students-list', views.students_list, name="t_students_list"),
    path('students-list/delete/<id>', views.delete_student, name="t_delete_student"),
    path('suggestions-list', views.suggestions_list, name="t_suggestions_list"),
    path('suggestions-list/confirm/<id>', views.confirm_suggestion, name="t_confirm_suggestion"),
]
