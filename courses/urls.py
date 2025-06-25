from django.urls import path
from courses.views import kurslar, courseList, details, getCoursesByCategory, getCoursesByCategoryId

urlpatterns = [
    path("", kurslar, name="kurslar"),
    path("list", courseList, name="course-list"),
    path("<kurs_adi>", details, name="details"),
    path("kategori/<int:category_id>", getCoursesByCategoryId, name="category_by_id"),
    path("kategori/<str:category>", getCoursesByCategory, name="category_by_slug"),
]
