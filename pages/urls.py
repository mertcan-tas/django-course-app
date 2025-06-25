from django.urls import path
from pages.views import index, hakkimizda, iletisim

urlpatterns = [
    path("", index, name="index"),
    path("hakkimizda/", hakkimizda, name="hakkimizda"),
    path("iletisim/", iletisim, name="iletisim"),
]
