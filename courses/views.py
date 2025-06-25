from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse("Kurslar")

def details(request):
    return HttpResponse("kurs detay")