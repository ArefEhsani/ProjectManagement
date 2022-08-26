from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from administration.models import Project
from accounts.models import CollegeUsers
from .models import ProjectSetting, ReportParts, ProjectReport, FinalReport
from django.contrib.auth.models import User

from teachers import models

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


def reports_list(request):
    all_part_objects = ReportParts.objects.all()
    if not all_part_objects:
        for r in range(1, 9):
            ReportParts.objects.create(number=r, is_active=True)
        return redirect(reverse('t_reports_list'))
    if request.method == "POST":
        selected = request.POST.getlist("report_number")
        for part in all_part_objects:
            if str(part.id) in selected:
                part.is_active = True
            else:
                part.is_active = False
            part.save()
        return redirect(reverse('t_reports_list'))
    context = {
        'active_tab': 'reports_list',
        'report_parts': all_part_objects,
        'reports': ProjectReport.objects.all(),
    }
    return render(request, 'teachers/List Reports.html', context)


def report_detail(request, id):
    report = get_object_or_404(ProjectReport, id=id)
    if request.method == "POST":
        mark = request.POST.get('mark')
        report.mark = mark
        report.save()
        return redirect(reverse('t_reports_list'))
    context = {
        'active_tab': 'report_detail',
        'report': report,
    }
    return render(request, 'teachers/Reports.html', context)


def final_reports_list(request):
    context = {
        'active_tab': 'final_reports_list',
        'final_reports': FinalReport.objects.filter(is_archive=False)
    }
    return render(request, 'teachers/Final Reports.html', context)


def final_report_detail(request, id):
    report = get_object_or_404(FinalReport, id=id)
    if request.method == "POST":
        mark = request.POST.get('mark')
        description = request.POST.get('description')
        report.mark = mark
        report.description = description
        report.is_archive = True
        report.save()
        return redirect(reverse('t_final_reports_list'))
    context = {
        'active_tab': 'final_report_detail',
        'report': report,
    }
    return render(request, 'teachers/Final.html', context)


def archive_report_list(request):
    context = {
        'active_tab': 'archive_report_list',
        'archive_reports': FinalReport.objects.filter(is_archive=True)
    }
    return render(request, 'teachers/Archive.html', context)


def archive_report_detail(request, id):
    report = get_object_or_404(FinalReport, id=id)
    context = {
        'active_tab': 'archive_report_detail',
        'report': report,
    }
    return render(request, 'teachers/Final Archive.html', context)
