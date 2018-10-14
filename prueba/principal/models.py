from django.db import models

class DatosGenerales(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Usuarios(models.Model):
    UserName = models.CharField(max_length=50)
