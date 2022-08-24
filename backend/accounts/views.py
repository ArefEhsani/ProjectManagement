from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/administrator/')
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
