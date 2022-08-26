from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from accounts.models import CollegeUsers
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project
from teachers.models import FinalReport, ProjectReport
# Create your views here.


@login_required
def teachers_list(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username, first_name=firstname, last_name=lastname, password=password)
        CollegeUsers.objects.create(
            user=user, firstname=firstname, lastname=lastname, is_teacher=True, is_student=False)
        return redirect(reverse("a_teachers_list"))

    context = {
        'teachers': CollegeUsers.objects.filter(is_teacher=True),
        'active_tab': 'teachers_list',
    }
    return render(request, "administration/List Professor.html", context)


@login_required
def delete_teacher(request, id):
    teacher = get_object_or_404(CollegeUsers, id=id)
    user = User.objects.get(id=teacher.user.id)
    user.delete()
    return redirect(reverse("a_teachers_list"))


@login_required
def students_list(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username, first_name=firstname, last_name=lastname, password=password)
        CollegeUsers.objects.create(
            user=user, firstname=firstname, lastname=lastname, is_student=True, is_teacher=False)
        return redirect(reverse("a_students_list"))

    context = {
        'students': CollegeUsers.objects.filter(is_student=True, is_teacher=False),
        'active_tab': 'students_list',
    }
    return render(request, "administration/List Students.html", context)


@login_required
def delete_student(request, id):
    student = get_object_or_404(CollegeUsers, id=id)
    user = User.objects.get(id=student.user.id)
    user.delete()
    return redirect(reverse("a_students_list"))


def projects_list(request):
    context = {
        'projects': Project.objects.filter(is_suggested=False),
        'active_tab': 'projects_list',
    }
    return render(request, "administration/List projects.html", context)


def marks_list(request):
    context = {
        'active_tab': 'marks_list',
        'reports': FinalReport.objects.filter()
    }
    return render(request, 'administration/List Number.html', context)


def reports_list(request):
    context = {
        'active_tab': 'reports_list',
        'reports': ProjectReport.objects.all(),
    }
    return render(request, 'administration/List Reports.html', context)


def report_detail(request, id):
    report = get_object_or_404(ProjectReport, id=id)
    context = {
        'active_tab': 'report_detail',
        'report': report,
    }
    return render(request, 'administration/Reports.html', context)


def final_reports_list(request):
    context = {
        'active_tab': 'final_reports_list',
        'final_reports': FinalReport.objects.filter(is_archive=False)
    }
    return render(request, 'administration/Final Reports.html', context)


def final_report_detail(request, id):
    report = get_object_or_404(FinalReport, id=id)
    context = {
        'active_tab': 'final_report_detail',
        'report': report,
    }
    return render(request, 'administration/Final.html', context)


def archive_report_list(request):
    context = {
        'active_tab': 'archive_report_list',
        'archive_reports': FinalReport.objects.filter(is_archive=True)
    }
    return render(request, 'administration/Archive.html', context)


def archive_report_detail(request, id):
    report = get_object_or_404(FinalReport, id=id)
    context = {
        'active_tab': 'archive_report_detail',
        'report': report,
    }
    return render(request, 'administration/Final Archive.html', context)
