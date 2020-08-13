from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User


def user_login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("index_route")
    else:
        return render(request, "accounts/login.html", {"error": "Login failed"})


def user_logout(request):
    logout(request)
    return redirect("login_route")

