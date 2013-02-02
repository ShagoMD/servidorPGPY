#!/usr/bin/python
import os
os.chdir("/home/mehanika/workspace/servidorPGPY")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from publicidadGeolocalizada.models import *
from django.contrib.gis.geos import *
from django.contrib.auth.models import User


u = User.objects.get(username='prueba')

print u

p2 = PuntoDeInteres()
p2.nombre = 'prueba1'
p2.descripcion = 'Lugar prueba1'
p2.telefono = '9999786402'
p2.direccion = 'Calle prueba'
p2.categoria = 'prueba'
p2.paginaWeb = 'www.prueba.com'
p2.correoElectronico = 'prueba@prueba.com'
p2.rutaImagen = '/prueba'
p2.posicion = Point(-89.5905554294586,20.9579931014452,srid=4326)
p2.propietario = u

p2.save()


