from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import CollegeUsers
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.


@login_required
def teachers_list(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(username=username, password=password)
        CollegeUsers.objects.create(user=user, firstname=firstname, lastname=lastname, is_teacher=True)
        return redirect(reverse("teachers_list"))

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
    return redirect(reverse("teachers_list"))


@login_required
def students_list(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(username=username, password=password)
        CollegeUsers.objects.create(user=user, firstname=firstname, lastname=lastname, is_student=True)
        return redirect(reverse("students_list"))

    context = {
        'students': CollegeUsers.objects.filter(is_student=True),
        'active_tab': 'students_list',
    }
    return render(request, "administration/List Students.html", context)


@login_required
def delete_student(request, id):
    student = get_object_or_404(CollegeUsers, id=id)
    user = User.objects.get(id=student.user.id)
    user.delete()
    return redirect(reverse("students_list"))
