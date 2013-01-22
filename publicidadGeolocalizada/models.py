from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class PuntoDeInteres(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    paginaWeb = models.CharField(max_length=80)
    correoElectronico = models.CharField(max_length=80)
    rutaImagen = models.CharField(max_length=150)
    posicion = models.PointField()
    objects = models.GeoManager()

class Anuncio(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=250)
    categoria = models.CharField(max_length=60)
    rutaImagen = models.CharField(max_length=150)
    propietario = models.ForeignKey(PuntoDeInteres)
