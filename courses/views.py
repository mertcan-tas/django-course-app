from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


data = {
    "programlama": "programlama kategorisine ait kurslar",
    "yapay-zeka": "yz kategorisine ait kurslar",
    "mobil": "mobil programlama kategorisine ait kurslar",
}

def index(request):
    return render(request, "courses/index.html")
    
def courseList(request):
    return HttpResponse("Kurs Listesi")

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")

def getCoursesByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("kategori bulunamadı")

def getCoursesByCategoryId(request, category_id):
    redirect_url = reverse('category_by_slug', args=["yapay-zeka"])
    return redirect(redirect_url)
