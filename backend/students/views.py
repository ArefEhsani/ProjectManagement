from django.shortcuts import render, redirect
from django.urls import reverse
from teachers.models import Project
from django.contrib.auth.models import User
from accounts.models import CollegeUsers
from teachers.models import Project
# Create your views here.


def get_project(request):
    user = User.objects.get(id=request.user.id)
    student = CollegeUsers.objects.get(user=user)
    if request.method == "POST":
        selected = request.POST.get("projects")
        project = Project.objects.get(id=selected)
        student.project = project
        student.save()
    context = {
        'active_tab': 'get_project',
        'projects': Project.objects.filter(is_suggested=False),
    }
    return render(request, 'students/Project Selection.html', context)


def project_suggestion(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        title = request.POST.get("title")
        type = request.POST.get("type")
        number_of_students = request.POST.get("number_of_students")
        description = request.POST.get("description")
        Project.objects.create(title=title, creator=user, type=type, number_of_students=number_of_students, description=description, is_suggested=True)
        return redirect(reverse("s_project_suggestion"))
    context = {
        'active_tab': 'project_suggestion',
    }
    return render(request, 'students/project proposal', context)


def report_parts_list(request):
    pass
