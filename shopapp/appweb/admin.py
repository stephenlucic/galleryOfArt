from django.contrib import admin
from .models import *

# Register your models here.
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','estado']
    list_editable = ['nombre']
    search_fields = ['rut']
    list_filter = ['estado']

admin.site.register(Tipo)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Contacto)