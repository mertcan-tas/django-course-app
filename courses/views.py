from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse("Kurslar")

def courseList(request):
    return HttpResponse("Kurs Listesi")

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")

def getCoursesByCategory(request, category):
    return HttpResponse(f"Kurs Kategorisi: {category}")

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)
