###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D
from api_Usuario import *
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
    pdb.set_trace()
    if parametrosValidos:
        
         posicionActual = Point(float(longitud),float(latitud),SRID)
         
         listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(nombre__contains=searchString)

    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return listaPuntosDeInteres;


def obtenerListadoPuntosDeInteresSearchCategoria(latitud, longitud, rangoMaximoAlcance, searchString, categoria):
   
    parametrosValidos = validarParametrosListadoPuntosDeInteresSearchCategoria(latitud, longitud, rangoMaximoAlcance, searchString, categoria)
    listaPuntosDeInteres = None

    if parametrosValidos:
        
         posicionActual = Point(float(longitud),float(latitud),SRID)
         
         if categoria == "nombre":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(nombre__contains=searchString)
             
         elif categoria == "categoria":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(categoria__contains=searchString)
             
         elif categoria == "descripcion":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(descripcion__contains=searchString)
         
         elif categoria == "direccion":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(direccion__contains=searchString)
         else:
             raise Exception("La categoria de busqueda es incorrecta");        
    else:
         raise Exception("Los valores de los parametros son incorrectos");
    
    return listaPuntosDeInteres;

def validarParametrosListadoPuntosDeInteres(latitud,longitud,rangoMaximoAlcance):
    parametrosValidos = True

    if latitud == None and not esTipoValido(latitud,TIPO_FLOTANTE):
       parametrosValidos = False
       
    elif longitud != None and not esTipoValido(longitud,TIPO_FLOTANTE):
        parametrosValidos = False
        
    elif rangoMaximoAlcance == None and not esTipoValido(longitud,TIPO_FLOTANTE):    
         parametrosValidos = False
         
    
    return parametrosValidos

def validarParametrosListadoPuntosDeInteresSearch(latitud,longitud,rangoMaximoAlcance,searchString):
    parametrosValidos = True
     
    if not validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance):
        parametrosValidos = False
    elif searchString == None or not esTipoValido(searchString,TIPO_CADENA):
        parametrosValidos = False
    
    return parametrosValidos

def validarParametrosListadoPuntosDeInteresSearchCategoria(latitud,longitud,rangoMaximoAlcance,searchString,categoria):
    parametrosValidos = True
     

    if not validarParametrosListadoPuntosDeInteres(latitud, longitud, rangoMaximoAlcance):
        parametrosValidos = False
    if searchString == None or not esTipoValido(searchString,TIPO_CADENA):
        parametrosValidos = False
    if categoria == None or not esTipoValido(categoria,TIPO_CADENA):
        parametrosValidos = False
        
    return parametrosValidos

def sonParametrosValidosRegistroPDI(usuario,nombre,categoria,latitud,longitud):
    if usuario==None or not esTipoValido(usuario,TIPO_CADENA):
        return False;
    if nombre==None or not esTipoValido(nombre,TIPO_CADENA):
        return False;
    if categoria==None or not esTipoValido(categoria,TIPO_ENTERO):
        return False;
    if latitud==None or not esTipoValido(latitud,TIPO_FLOTANTE):
        return False;
    if longitud==None or not esTipoValido(longitud,TIPO_FLOTANTE):
        return False;
    return True;

def registrarPuntoDeInteres(camposObligatorios):
    usuarioValido=esUsuarioValido(camposObligatorios["usuario"]);
    try:
        cat=Categoria.objects.get(pk=int(camposObligatorios["categoria"]))
        if usuarioValido is not False:
            listaPDI=PuntoDeInteres.objects.filter(propietario__email__exact=camposObligatorios["usuario"]);
            if(len(listaPDI)<3):
                posicionNueva=Point(float(camposObligatorios["latitud"]),float(camposObligatorios["longitud"]),SRID)
                listaPDIPosiciones=PuntoDeInteres.objects.filter(posicion__exact=posicionNueva);
                if(len(listaPDIPosiciones)==0):
                    nuevoPDI=PuntoDeInteres();
                    nuevoPDI.nombre=camposObligatorios["nombre"];
                    nuevoPDI.categoria=cat;
                    nuevoPDI.propietario=usuarioValido;
                    nuevoPDI.posicion=Point(float(camposObligatorios["latitud"]),float(camposObligatorios["longitud"]),srid=SRID)
                    nuevoPDI.save();
                    return 0;
                else:
                    return 1;
            else:
                return 2;
        else:
            return 3;
    except Exception,err:
        return 4;
