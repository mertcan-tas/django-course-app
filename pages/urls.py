from django.urls import path
from courses.views import IndexView
from pages.views import AboutView, ContactView

urlpatterns = [
    path("", IndexView, name="index"),
    path("about/", AboutView, name="about"),
    path("contact/", ContactView, name="contact"),
]
