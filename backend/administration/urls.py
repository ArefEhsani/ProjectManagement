from django.urls import path
from . import views

urlpatterns = [
    path('teachers-list', views.teachers_list, name="a_teachers_list"),
    path('teachers-list/delete/<id>', views.delete_teacher, name="a_delete_teacher"),
    path('students-list', views.students_list, name="a_students_list"),
    path('students-list/delete/<id>', views.delete_student, name="a_delete_student"),
    path('projects-list', views.projects_list, name="a_projects_list"),
    path('marks-list', views.marks_list, name="a_mark_list"),
    path('reports-list', views.reports_list, name="a_reports_list"),
    path('reports-list/<id>', views.report_detail, name="a_report_detail"),
    path('final-reports-list', views.final_reports_list, name="a_final_reports_list"),
    path('final-reports-list/<id>', views.final_report_detail, name="a_final_report_detail"),
    path('archive-report-list', views.archive_report_list, name="a_archive_report_list"),
    path('archive-report-list/<id>', views.archive_report_detail, name="a_archive_report_detail"),
]
