from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('artistas/',artistas, name="artistas"),
    path('contacto', contacto, name="contacto"),
    path('mantenedor/agregar_artista/',agregar_artista, name="agregar_artista"),
    path('mantenedor/listar_artistas/', listar_artistas, name="listar_artistas"),
    path('mantenedor/modificar_artista/<rut>/', modificar_artista, name="modificar_artista"),
    path('mantenedor/eliminar_artista/<rut>/', eliminar_artista, name="eliminar_artista"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro/', registro, name="registro")

]