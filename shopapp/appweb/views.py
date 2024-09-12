from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def profesionales(request):
    return render(request, "profesionales.html")

def contacto(request):
    return render(request, "contacto.html")

