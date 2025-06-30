from django.urls import path
from courses.views import index, details, getCoursesByCategory, create_course, courseList, edit_course, delete_course

urlpatterns = [
    path("", index, name="index"),
    path("create-course", create_course, name="create-course"),
    path("edit-course/<slug:slug>", edit_course, name="edit-course"),
    path("delete-course/<slug:slug>", delete_course, name="delete-course"),
    path("course-list", courseList, name="course-list"),
    path("<slug:slug>", details, name="course-detail"),
    path("kategori/<slug:slug>", getCoursesByCategory, name="course-category"),
]