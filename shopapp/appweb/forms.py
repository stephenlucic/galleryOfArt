from django import forms
from .models import Contacto, Artista

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"
        
class ArtistaForm(forms.ModelForm):
    
    class Meta:
        model = Artista
        fields = "__all__"
        
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type':'date'}, format=('%Y-%m-%d'))
        }


