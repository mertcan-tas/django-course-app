# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("account/", include("account.urls")),
    path("kurslar/", include("courses.urls")),
]