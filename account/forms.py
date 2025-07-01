from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms import widgets
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class": "form-control"})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            self.add_error("email", "email is exists")
        return email
        

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class": "form-control"})