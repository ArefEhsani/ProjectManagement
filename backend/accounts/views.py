from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import CollegeUsers
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def handler404(request, exception):
    return render(request, 'http_status/404.html', status=404)


def login_page(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        student = CollegeUsers.objects.get(user=user)
        if student.is_student:
            return redirect(reverse('s_get_project'))
        elif student.is_teacher:
            return redirect(reverse('t_student_permissions'))
        else:
            return redirect(reverse('a_teachers_list'))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return render(request, 'accounts/index.html', {"wrong_auth": True})
    context = {}
    return render(request, 'accounts/index.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
