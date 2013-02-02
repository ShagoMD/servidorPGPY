###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D

###Variables globales
SRID=4326


def obtenerListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
   # print latitud,longitud,rangoMaximoAlcance
   
    parametrosValidos = validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance=11)
    puntoDeInteres = None
    if parametrosValidos:
         print "Parametros validos"
         posicionActual = Point(float(longitud),float(latitud),SRID)
         puntoDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=7)))
         
    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return puntoDeInteres;



def validarParametrosListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    parametrosValidos = True
    
    if latitud == None and not esTipoValido(latitud,TIPO_FLOTANTE):
       parametrosValidos = False
    if longitud != None and not esTipoValido(longitud,TIPO_FLOTANTE):
        parametrosValidos == False
    if rangoMaximoAlcance == None and not esTipoValido(longitud,TIPO_ENTERO):    
        parametrosValidos = False
    
    return parametrosValidos