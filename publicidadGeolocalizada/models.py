#from django.db import models
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
    posicion = models.PointField(srid=4326)
    altitud = models.FloatField(default=0.0)
    objects = models.GeoManager()
    favoritos = models.ManyToManyField(User, related_name = 'favoritos')
    propietario = models.ForeignKey(User, related_name = 'propiedades')           
    
    def dehydrate(self, bundle):
        # remove unneeded point-field from the response data
        del bundle.data['posicion']
        # add required fields back to the response data in the form we need it
        bundle.data['lat'] = bundle.obj.posicion.y
        bundle.data['lng'] = bundle.obj.posicion.x
        return bundle 



class Anuncio(models.Model):
    anunciante = models.ForeignKey(PuntoDeInteres)
    titulo = models.CharField(max_length=180)
    descripcion = models.CharField(max_length=500)
    categoria = models.CharField(max_length=120)
    rutaImagen = models.CharField(max_length=500)
    
#class Usuario(models.Model):
#   correoElectronico=models.CharField(max_length=100,unique=True)
#    contrasenia=models.CharField(max_length=24)
