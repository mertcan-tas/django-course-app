from django.urls import path
from courses.views import (
    IndexView, 
    CreateCourseView, CourseListView, EditCourseView, DeleteCourseView,
    CourseDetailView, CourseCategoryView,
)

urlpatterns = [
    path("", IndexView, name="index"),
    path("create-course", CreateCourseView, name="create-course"),
    path("course-list", CourseListView, name="course-list"),
    path("edit-course/<slug:slug>", EditCourseView, name="edit-course"),
    path("delete-course/<slug:slug>", DeleteCourseView, name="delete-course"),
    path("<slug:slug>", CourseDetailView, name="course-detail"),
    path("kategori/<slug:slug>", CourseCategoryView, name="course-category"),
]