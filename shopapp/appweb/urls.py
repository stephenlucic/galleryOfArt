from django.urls import path
from .views import home,artistas, contacto, agregar_artista

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('artistas/',artistas, name="artistas"),
    path('contacto', contacto, name="contacto"),
    path('mantenedor/agregar_artistas/',agregar_artista, name="agregar_artistas")

]