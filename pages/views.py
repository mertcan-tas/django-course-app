from django.http import HttpResponse

def home(request):
    return HttpResponse("anasayfa")
    
def hakkimizda(request):
    return HttpResponse("hakkimizda")

def iletisim(request):
    return HttpResponse("iletisim")