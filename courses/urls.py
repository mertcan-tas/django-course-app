from django.urls import path
from courses.views import index, details, getCoursesByCategory, create_course

urlpatterns = [
    path("", index, name="index"),
    path("create-course", create_course, name="create-course"),
    path("<slug:slug>", details, name="course-detail"),
    path("kategori/<slug:slug>", getCoursesByCategory, name="course-category"),
]