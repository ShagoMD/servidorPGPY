###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D
from utilidades import *
from strings import *
import pdb
SRID=4326
MAXIMO_PDI_REGISTRADOS=20

CODIGO_REGISTRO_EXITOSO=0;
CODIGO_LOCALIZACION_REPETIDA=1;
CODIGO_LIMITE_PDI_ALCANZADO=2;
CODIGO_USUARIO_INVALIDO=3;
CODIGO_CATEGORIA_INVALIDA=4

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
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(nombre__icontains=searchString)
             
         elif categoria == "categoria":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(categoria__icontains=searchString)
             
         elif categoria == "descripcion":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(descripcion__icontains=searchString)
         
         elif categoria == "direccion":
             listaPuntosDeInteres =  PuntoDeInteres.objects.filter(posicion__distance_lte=(posicionActual, D(km=rangoMaximoAlcance))).filter(direccion__icontains=searchString)
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

def sonParametrosObligatoriosPDIValidos(parametros):
    usuario=parametros['usuario'];
    nombre=parametros['nombre'];
    categoria=parametros['categoria'];
    latitud=parametros['latitud'];
    longitud=parametros['longitud'];
    altitud=parametros['altitud'];
    
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
    if altitud==None or not esTipoValido(altitud,TIPO_FLOTANTE):
        return False;
    return True;

def sonParametrosOpcionalesPDIValidos(parametros):
    descripcion=parametros["descripcion"];
    direccion=parametros["direccion"];
    paginaWeb=parametros["paginaWeb"];
    telefono=parametros["telefono"];
    email=parametros["email"];
    urlImagen=parametros["imagen"];
    
    if descripcion!="" and not esTipoValido(descripcion,TIPO_CADENA):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;
    if direccion!="" and not esTipoValido(direccion,TIPO_CADENA):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;
    if paginaWeb!="" and not esURLValida(paginaWeb):
        return PDI_MENSAJE_URL_WEB_INVALIDA;
    if telefono!="" and not esTipoValido(telefono,TIPO_ENTERO):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;
    if email!="" and not esCorreoValido(email):
        return PDI_MENSAJE_CORREO_INVALIDO;
    if urlImagen!="" and not esURLValida(urlImagen):
        return PDI_MENSAJE_URL_IMAGEN_INVALIDA;

    return True;

def registrarPuntoDeInteres(camposObligatorios,camposOpcionales):
    usuarioValido=esUsuarioValido(camposObligatorios["usuario"]);
    if usuarioValido is not False:            
        listaPDI=PuntoDeInteres.objects.filter(propietario__email__exact=camposObligatorios["usuario"]);
        if(len(listaPDI)<MAXIMO_PDI_REGISTRADOS):
            posicionNueva=Point(float(camposObligatorios["longitud"]),float(camposObligatorios["latitud"]),srid=SRID);
            listaPDIPosiciones=PuntoDeInteres.objects.filter(posicion__exact=posicionNueva,altitud__exact=camposObligatorios['altitud']);
            if(len(listaPDIPosiciones)==0):
                try:
                    cat=Categoria.objects.get(pk=int(camposObligatorios["categoria"]))
                    nuevoPDI=PuntoDeInteres();
                    guardarPuntoDeInteres(usuarioValido,posicionNueva,camposObligatorios,camposOpcionales,nuevoPDI);
                    
                    return CODIGO_REGISTRO_EXITOSO;    
                except Exception,err:
                    return CODIGO_CATEGORIA_INVALIDA;
            else:
                return CODIGO_LOCALIZACION_REPETIDA;
        else:
            return CODIGO_LIMITE_PDI_ALCANZADO;
    else:
        return CODIGO_USUARIO_INVALIDO;

def guardarPuntoDeInteres(usuario,posicion,camposObligatorios,camposOpcionales,pdi):                    
    cat=Categoria.objects.get(pk=int(camposObligatorios["categoria"]))

    #campos obligatorios
    pdi.nombre=camposObligatorios["nombre"];
    pdi.categoria=cat;
    pdi.propietario=usuario;
    pdi.posicion=posicion;
    pdi.altitud=float(camposObligatorios['altitud']);
    #campos opcionales
    pdi.descripcion=camposOpcionales['descripcion'];
    pdi.direccion=camposOpcionales['direccion'];
    pdi.paginaWeb=camposOpcionales['paginaWeb'];
    pdi.telefono=camposOpcionales['telefono'];
    pdi.correoElectronico=camposOpcionales['email'];
    pdi.rutaImagen=camposOpcionales['imagen'];
    
    pdi.save();
    return;

def obtenerPDIsDeUsuario(usuario):
    usuarioValido=esUsuarioValido(usuario);
    if usuarioValido is not False: 
        listaPDI=PuntoDeInteres.objects.filter(propietario__email__exact=usuario);
        return listaPDI;
    else:    
        return CODIGO_USUARIO_INVALIDO;
    
    
    
    
    
