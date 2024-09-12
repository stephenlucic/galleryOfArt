from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def artistas(request):
    return render(request, "artistas.html")

def contacto(request):

    data = {
        "form_contacto": ContactoForm,
        "mensaje":""
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Datos Guardados con éxito"
        else:
            data["mensaje"] = "Error"
            data["form_contacto"] = formulario    

    return render(request, "contacto.html", data) 

def agregar_artista(request):
    return render(request, "mantenedor/artistas/agregar.html")

