from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "pages/index.html")
    
def hakkimizda(request):
    return render(request, "pages/about.html")

def iletisim(request):
    return render(request, "pages/contact.html")