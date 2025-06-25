from django.urls import path
from courses.views import kurslar, details

urlpatterns = [
    path("", kurslar, name="kurslar"),
    path("details/", kurslar, name="details"),
]
