###Imports
from models import *
from django.contrib.gis.geos import *

###Variables globales
SRID=4326


def obtenerListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    parametrosValidos = validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance)
    if parametrosValidos:
         posicionActual = Point(float(longitud),float(latitud),SRID)
         PuntoDeInteres.objects.filter(point__distance_lte=(posicionActual, D(km=7)))
    else:
        print 1
    



def validarParametrosListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    if latitud == None and type(latitud)!='float':
        return false
    if longitud == None:
        return false
    if rangoMaximoAlcance == None:    
        return false