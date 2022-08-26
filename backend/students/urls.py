from django.urls import path
from . import views
urlpatterns = [
    path('get-project', views.get_project, name="s_get_project"),
    path('suggest', views.project_suggestion, name="s_suggest_project"),
    path('report-parts', views.report_parts_list, name="s_report_parts"),
    path('report-parts/<id>', views.report_part_detail, name="s_report_detail"),
    path('final-report', views.student_final_report, name="s_final_report"),
]
