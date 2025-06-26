from django.urls import path
from courses.views import index, details, getCoursesByCategory

urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>", details, name="course-detail"),
    path("kategori/<slug:slug>", getCoursesByCategory, name="course-category"),
]