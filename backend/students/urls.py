from django.urls import path
from . import views
urlpatterns = [
    path('get-project', views.get_project, name="s_get_project"),
]
