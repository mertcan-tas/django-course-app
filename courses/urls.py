from django.urls import path
from courses.views import index, courseList, details, getCoursesByCategory, getCoursesByCategoryId

urlpatterns = [
    path("", index, name="index"),
    path("list", courseList, name="course-list"),
    path("<slug:course_slug>", details, name="course_details"),
    path("kategori/<int:category_id>", getCoursesByCategoryId, name="courses_by_category_id"),
    path("kategori/<slug:category_slug>", getCoursesByCategory, name="courses_by_category"),
]