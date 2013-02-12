###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D
import pdb
SRID=4326


def obtenerListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
   
    parametrosValidos = validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance=11)
    listaPuntosDeInteres = None
    if parametrosValidos:
        
         posicionActual = Point(float(longitud),float(latitud),SRID)
         listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance)))

    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return listaPuntosDeInteres;


def obtenerListadoPuntosDeInteresSearch(latitud, longitud, rangoMaximoAlcance, searchString):
   
    parametrosValidos = validarParametrosListadoPuntosDeInteresSearch(latitud, longitud, rangoMaximoAlcance, searchString)
    listaPuntosDeInteres = None

    if parametrosValidos:
        
         posicionActual = Point(float(longitud),float(latitud),SRID)
         
         listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(m=rangoMaximoAlcance))).filter(nombre__contains=searchString)

    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return listaPuntosDeInteres;


def validarParametrosListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    parametrosValidos = True

    if latitud == None and not esTipoValido(latitud,TIPO_FLOTANTE):
       parametrosValidos = False
    if longitud != None and not esTipoValido(longitud,TIPO_FLOTANTE):
        parametrosValidos == False
    if rangoMaximoAlcance == None and not esTipoValido(rangoMaximoAlcance,TIPO_ENTERO):    
        parametrosValidos = False
    
    return parametrosValidos

def validarParametrosListadoPuntosDeInteresSearch(latitud,longitud,rangoMaximoAlcance,searchString):
    parametrosValidos = True
     
    if latitud == None and not esTipoValido(latitud,TIPO_FLOTANTE):
       parametrosValidos = False
    if longitud != None and not esTipoValido(longitud,TIPO_FLOTANTE):
        parametrosValidos == False
    if rangoMaximoAlcance == None and not esTipoValido(rangoMaximoAlcance,TIPO_ENTERO):    
        parametrosValidos = False
    if searchString == None or not esTipoValido(searchString,TIPO_CADENA):
        parametrosValidos = False
    
    return parametrosValidos


