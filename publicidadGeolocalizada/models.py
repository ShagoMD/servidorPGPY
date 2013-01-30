from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
# Create your models here.


class PuntoDeInteres(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=310)
    categoria = models.CharField(max_length=120)
    paginaWeb = models.CharField(max_length=500)
    correoElectronico = models.CharField(max_length=120)
    rutaImagen = models.CharField(max_length=310)
    posicion = models.PointField()
    objects = models.GeoManager()
    favoritos = models.ManyToManyField(User,editable=False, related_name = 'favoritos')
    pripietario = models.ForeignKey(User, editable=False, related_name = 'propiedades')           
     



class Anuncio(models.Model):
    anunciante = models.ForeignKey(PuntoDeInteres)
    titulo = models.CharField(max_length=180)
    descripcion = models.CharField(max_length=500)
    categoria = models.CharField(max_length=120)
    rutaImagen = models.CharField(max_length=500)
    
    
