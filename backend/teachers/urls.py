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
    path('reports_list', views.reports_list, name="t_reports_list"),
    path('reports_list/<id>', views.report_detail, name="t_report_detail"),
    path('final-reports-list', views.final_reports_list, name="t_final_reports_list"),
    path('final-reports-list/<id>', views.final_report_detail, name="t_final_report_detail"),
    path('archive-report-list', views.archive_report_list, name="t_archive_report_list"),
    path('archive-report-list/<id>', views.archive_report_detail, name="t_archive_report_detail"),
]
