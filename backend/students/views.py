from django.shortcuts import render, redirect
from django.urls import reverse
from teachers.models import Project
from django.contrib.auth.models import User
from accounts.models import CollegeUsers
from teachers.models import Project, ReportParts, ProjectReport, FinalReport, ProjectSetting
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from django.db.models import Count


def get_project(request):
    status = ProjectSetting.objects.last()
    if not status.can_get:
        raise Http404()
    user = User.objects.get(id=request.user.id)
    student = CollegeUsers.objects.get(user=user)
    if request.method == "POST":
        selected = request.POST.get("projects")
        project = Project.objects.get(id=selected)
        student.project = project
        student.save()
    projects_user = Project.objects.filter(is_suggested=False).annotate(number_of_taken=Count('collegeusers'))
    context = {
        'active_tab': 'get_project',
        'projects': projects_user,
    }
    return render(request, 'students/Project Selection.html', context)


def project_suggestion(request):
    status = ProjectSetting.objects.last()
    if not status.suggest:
        raise Http404()
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        title = request.POST.get("title")
        type = request.POST.get("type")
        number_of_students = request.POST.get("number_of_students")
        description = request.POST.get("description")
        Project.objects.create(title=title, creator=user, type=type, number_of_students=number_of_students, description=description, is_suggested=True)
        return redirect(reverse("s_suggest_project"))
    context = {
        'active_tab': 'project_suggestion',
    }
    return render(request, 'students/project proposal.html', context)


def report_parts_list(request):
    status = ProjectSetting.objects.last()
    if not status.reports:
        raise Http404()
    context = {
        'active_tab': 'report_parts_list',
        'report_parts': ReportParts.objects.filter(is_active=True),
    }
    return render(request, 'students/Report project.html', context)


def report_part_detail(request, id):
    status = ProjectSetting.objects.last()
    if not status.reports:
        raise Http404()
    part = get_object_or_404(ReportParts, id=id)
    user = User.objects.get(id=request.user.id)
    student = CollegeUsers.objects.get(user=user)
    student_part_report = ProjectReport.objects.filter(student=student, number=id).first()
    if not part.is_active:
        raise Http404()
    if request.method == "POST":
        file = request.FILES.get("report_file")
        description = request.POST.get("description")
        obj, created = ProjectReport.objects.get_or_create(student=student, number=id, defaults={'file': file, 'description': description})
        return redirect(reverse("s_report_parts"))
    context = {
        'active_tab': 'report_part_detail',
        'student_report': student_part_report,
        'number': id,
    }
    return render(request, 'students/Reports.html', context)


def student_final_report(request):
    status = ProjectSetting.objects.last()
    if not status.final_report:
        raise Http404()
    user = User.objects.get(id=request.user.id)
    student = CollegeUsers.objects.get(user=user)
    final_report = FinalReport.objects.filter(student=student).first()
    if request.method == "POST":
        final_project = request.FILES.get("final_project")
        description = request.POST.get("description")
        obj, created = FinalReport.objects.get_or_create(student=student, defaults={'file': final_project, 'description': description})
        return redirect(reverse("s_final_report"))
    context = {
        'active_tab': 'student_final_report',
        'final_report': final_report,
    }
    return render(request, 'students/Final project.html', context)
