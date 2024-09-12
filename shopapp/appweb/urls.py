from django.urls import path
from .views import home, profesionales, contacto

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('profesionales/',profesionales, name="profesionales"),
    path('contacto', contacto, name="contacto")

]