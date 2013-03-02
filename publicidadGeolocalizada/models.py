#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
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
    posicion = models.PointField(srid=4326)
#    altitud = models.FloatField(default=0.0)	
    favoritos = models.ManyToManyField(User, related_name = 'favoritos')
    propietario = models.ForeignKey(User, related_name = 'propiedades')
    objects = models.GeoManager()
    


class Anuncio(models.Model):
    anunciante = models.ForeignKey(PuntoDeInteres)
    titulo = models.CharField(max_length=180)
    descripcion = models.CharField(max_length=500)
    categoria = models.CharField(max_length=120)
    rutaImagen = models.CharField(max_length=500)
    

class Imagen(models.Model):
    imagen = ImageWithThumbsField(upload_to='logo', sizes=((125,125),(200,200)))
    #nombre = models.CharField(max_length=200)
    #imagen = models.ImageField(upload_to='logo')
    

