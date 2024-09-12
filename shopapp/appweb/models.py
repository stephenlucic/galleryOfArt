from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Artista(models.Model):
    rut= models.CharField(max_length=10, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=400, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="artista", null=True)
    
    def __str__(self):
        return self.nombre
    
tipo_contacto=[
    [0,"sugerencia"],
    [1,"reclamos"],
    [2,"consultas"]
    ]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    tipo_contacto = models.IntegerField(choices=tipo_contacto)
    mensaje= models.TextField()

    def __str__(self):
        return self.nombre+" "+self.email
    