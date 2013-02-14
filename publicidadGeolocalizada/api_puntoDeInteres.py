###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D
import pdb
###Variables globales
SRID=4326


def obtenerListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
   # print latitud,longitud,rangoMaximoAlcance
   
    parametrosValidos = validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance=11)
    listaPuntosDeInteres = None
    if parametrosValidos:
         #print "Parametros validos"
         posicionActual = Point(float(longitud),float(latitud),SRID)
         #listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__dwithin=(posicionActual, D(km=rangoMaximoAlcance)))
         listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance)))
        
        
          #  print pdi.posicion.get_x()
    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return listaPuntosDeInteres;



def validarParametrosListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    parametrosValidos = True
    #pdb.set_trace()
    if latitud == None and not esTipoValido(latitud,TIPO_FLOTANTE):
       parametrosValidos = False
       
    elif longitud != None and not esTipoValido(longitud,TIPO_FLOTANTE):
        parametrosValidos = False
        
    elif rangoMaximoAlcance == None and not esTipoValido(longitud,TIPO_ENTERO):    
         parametrosValidos = False
         
    
    return parametrosValidos