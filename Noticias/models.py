from django.db import models

# Create your models here.
from django.utils import timezone

class Noticia (models.Model):
    titulo= models.CharField(max_length=200)
    fecha= models.DateTimeField()
    texto= models.TextField()
    
    def __str__(self):
        return self.titulo
    
class Comentario (models.Model):
    fecha=models.DateTimeField()
    nombre=models.CharField(max_length=200)
    texto= models.TextField()

    def __str__(self):
        return self.nombre
    
