from django.urls import path
from .views import home,artistas, contacto

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('artistas/',artistas, name="artistas"),
    path('contacto', contacto, name="contacto"),
    path('mantenedor/agregar_artistas/',)

]