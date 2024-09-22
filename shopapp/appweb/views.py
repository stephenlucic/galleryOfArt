from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,Group


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
    
    data = {
        "form_artista": ArtistaForm,
        "mensaje":""
    }
    
    if request.method == 'POST':
        formulario = ArtistaForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Artista creado exitosamente"
        else:
            data["mensaje"]="Error"
            data["form_artista"]=formulario
        
    
    return render(request, "mantenedor/artistas/agregar.html", data)

def listar_artistas(request):
    
    artistas = Artista.objects.all()
    
    data={
        'mis_artistas': artistas
    }
    return render(request, "mantenedor/artistas/listar.html",data)

def modificar_artista(request, rut):
    
    artista = get_object_or_404(Artista, rut=rut)
    
    data={
        'form_artista': ArtistaForm(instance=artista)
    }
    
    if request.method == "POST":
        formulario = ArtistaForm(data=request.POST, instance=artista, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_artistas")
        else:
            data["mensaje"] = "Error"
            data["form"]= formulario
    
    return render(request,"mantenedor/artistas/modificar.html",data)

def eliminar_artista(request, rut):
    
    artista = get_object_or_404(Artista, rut=rut)
    artista.delete() 
    
    return redirect(to="listar_artistas")

def login_usuario(request):
    
    
    print("Bienvenido: "+ request.user.username)
    
    if request.user.groups.filter(name="Artista"):
        print("es un artista")
    
    return redirect(to='home')

def registro(request):
    
    data={
        "mensaje":""
    }
    
    if request.method == "POST":
        nombre=request.POST.get("nombre")
        apellido=request.POST.get("apellido")
        correo=request.POST.get("correo")
        password=request.POST.get("password")
        
        usu = User()
        usu.set_password(password)
        usu.username=nombre
        usu.email=correo
        usu.first_name=nombre
        usu.last_name=apellido
        
        grupo = Group.objects.get(name="Artista")
        
        try:
            usu.save()
            usu.groups.add(grupo)
            #data["mensaje"]="Usuario creado exitosamente"
            user = authenticate(username=usu.username,password=password)
            login(request,user)
            return redirect(to="home")
        
        except:
            data["mensaje"]="error"
        
    return render(request, "registration/registro.html")
    

