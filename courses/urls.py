from django.urls import path
from courses.views import kurslar, courseList, details, getCoursesByCategory, getCoursesByCategoryId

urlpatterns = [
    path("", kurslar, name="kurslar"),
    path("list", courseList, name="course-list"),
    path("<str:kurs_adi>", kurslar, name="details"),
    path("kategori/<str:category>", getCoursesByCategory, name="category"),
    path("kategori/<int:category_id>", getCoursesByCategoryId, name="category"),
]
