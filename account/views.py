from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def LoginView(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            context = {"error": "Kullanıcı adı veya parola hatalı."}
            return render(request, "account/login.html", context)
    else:
        return render(request, "account/login.html")

def RegisterView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "account/register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {"error": "Username is already taken"})

        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {"error": "Email is already registered"})

        User.objects.create_user(username=username, email=email, password=password1)
        return redirect('login')

    return render(request, "account/register.html")

@login_required
def LogoutView(request):
    logout(request)
    return redirect("login")
