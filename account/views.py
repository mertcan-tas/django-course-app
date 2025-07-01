from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import LoginUserForm

from django.contrib.auth.models import User

def LoginView(request):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginUserForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                form.username.add_error(None, "username or password is incorrect.")
    return render(request, "account/login.html", {"form": form})

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
