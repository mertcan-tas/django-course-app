from django.urls import path
from account.views import LoginView, RegisterView, PasswordChangeView, LogoutView

urlpatterns = [
    path("login", LoginView, name="login"),
    path("register", RegisterView, name="register"),
    path("change-password", PasswordChangeView, name="change-password"),
    path("logout", LogoutView, name="logout")
]