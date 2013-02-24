#!/usr/bin/python
import os
os.chdir("C:/Users/Eric/Favorites/Documents/Eclipse Projects/servidorPGPY")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from publicidadGeolocalizada.models import *
from django.contrib.auth.models import User


#from django.db import transaction
#transaction.rollback()
from django.db import connection
connection._rollback()


pdi = PuntoDeInteres.objects.get(id__exact=2)
a1 = Anuncio()
a1.anunciante = pdi
a1.titulo = 'Vacunas gratis'
a1.descripcion = 'Hoy ultimo día'
a1.rutaImagen = '/servicioMedico/vacunas'
a1.save()
