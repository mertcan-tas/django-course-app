from django.shortcuts import render
from django.http import HttpResponse
    
def AboutView(request):
    return render(request, "pages/about.html")

def ContactView(request):
    return render(request, "pages/contact.html")