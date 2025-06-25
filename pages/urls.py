from django.urls import path
from pages.views import home, hakkimizda, iletisim

urlpatterns = [
    path("", home, name="home"),
    path("hakkimizda/", hakkimizda, name="hakkimizda"),
    path("iletisim/", iletisim, name="iletisim"),
]
