from django.db import models

# Create your models here.

class Pais(models.Model) :
    id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=70)
    def __str__(self):
        return self.Nombre

class Trabajador(models.Model) :
    dni = models.CharField(max_length=12, primary_key=True)
    apellidos = models.CharField(max_length=70)
    nombres = models.CharField(max_length=70)
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    fechaNacimiento = models.DateField()
    foto = models.ImageField(upload_to='photos', default = 'photos/user.jpg')
