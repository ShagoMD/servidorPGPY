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
p2.nombre = 'Servicio Medico'
p2.descripcion = 'Servicio Medico'
p2.telefono = '99998945630'
p2.direccion = 'Servicio Medico UADY'
p2.categoria = 'PDI'
p2.paginaWeb = 'www.serviciomedico.uady.com'
p2.correoElectronico = 'serviciomedico@uady.mx'
p2.rutaImagen = '/fmat'
p2.posicion = Point(-89.62965,20.97965,srid=4326)
p2.propietario = u

p2.save()


#Crear anuncio
pdi = PuntoDeInteres.objects.get(id__exact=4)
a1 = Anuncio()
a1.anunciante = pdi
a1.titulo = 'Inicio del proceso de inscripción'
a1.descripcion = 'Este 20 de agosto inicia el proceso de inscripcion'
a1.rutaImagen = '/fmat/inscripcion'
a1.save()
