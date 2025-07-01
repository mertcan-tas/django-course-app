from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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
                form.add_error(None, "username or password is incorrect.")
    return render(request, "account/login.html", {"form": form})

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect("index")
        
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, "account/register.html", {"form": form})

@login_required
def PasswordChangeView(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed successfully!")
            return redirect("index")
        else:
            messages.error(request, "Password change failed. Please correct the errors.")
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, "account/change-password.html", {"form": form})

@login_required
def LogoutView(request):
    logout(request)
    return redirect("login")