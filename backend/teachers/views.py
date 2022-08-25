from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from administration.models import Project
from accounts.models import CollegeUsers
from .models import ProjectSetting
from django.contrib.auth.models import User

# Create your views here.


def student_permissions(request):
    project = ProjectSetting.objects.filter(id=1)
    if request.method == "POST":
        can_get = False if not request.POST.get("can_get") else True
        suggest = False if not request.POST.get("suggest") else True
        reports = False if not request.POST.get("reports") else True
        final_report = False if not request.POST.get("final_report") else True
        if project:
            project.update(can_get=can_get, suggest=suggest, reports=reports, final_report=final_report)
        else:
            ProjectSetting.objects.create(can_get=can_get, suggest=suggest, reports=reports, final_report=final_report)
        return redirect(reverse("t_student_permissions"))
    context = {
        'active_tab': 'student_permissions',
        'settings': project.last(),
    }
    return render(request, 'teachers/Parts Project.html', context)


def create_project(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        title = request.POST.get("title")
        type = request.POST.get("type")
        number_of_students = request.POST.get("number_of_students")
        description = request.POST.get("description")
        Project.objects.create(title=title, creator=user, type=type, number_of_students=number_of_students, description=description, is_suggested=False)
        return redirect("t_create_project")
    context = {
        'active_tab': 'create_project',
    }
    return render(request, 'teachers/Create project.html', context)


def projects_list(request):
    context = {
        'active_tab': 'projects_list',
        'projects': Project.objects.filter(is_suggested=False),
    }
    return render(request, 'teachers/List projects.html', context)


def students_list(request):
    context = {
        'active_tab': 'students_list',
        'students': CollegeUsers.objects.filter(is_student=True),
    }
    return render(request, 'teachers/List Students.html', context)


@login_required
def delete_student(request, id):
    student = get_object_or_404(CollegeUsers, id=id)
    user = User.objects.get(id=student.user.id)
    user.delete()
    return redirect(reverse("t_students_list"))


def suggestions_list(request):
    context = {
        'active_tab': 'suggestions_list',
        'suggestions': Project.objects.filter(is_suggested=True),
    }
    return render(request, 'teachers/List Suggestions.html', context)


def confirm_suggestion(request, id):
    suggestion = get_object_or_404(Project, id=id)
    suggestion.is_suggested = False
    suggestion.save()
    return redirect(reverse("t_suggestions_list"))
