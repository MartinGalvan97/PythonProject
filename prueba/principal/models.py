from django.db import models

class DatosGenerales(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
