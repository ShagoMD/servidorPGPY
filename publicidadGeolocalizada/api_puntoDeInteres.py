###Imports
from models import *
from django.contrib.gis.geos import *
from conversionTipos import *
from django.contrib.gis.measure import D
from utilidades import *
from strings import *
import pdb
import re

SRID=4326
MAXIMO_PDI_REGISTRADOS=20
REGEX=re.compile('\s+');

CODIGO_REGISTRO_EXITOSO=0;

CODIGO_LOCALIZACION_REPETIDA=1;
CODIGO_LIMITE_PDI_ALCANZADO=2;
CODIGO_USUARIO_INVALIDO=3;
CODIGO_CATEGORIA_INVALIDA=4;
CODIGO_PDI_NO_EXISTE=5;
CODIGO_PDI_ELIMINADO=6;
CODIGO_NO_HAY_PDIs_REGISTRADOS=7;



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

def sonParametrosObligatoriosPDIValidos(parametros):
    usuario=parametros['usuario'];
    nombre=parametros['nombre'];
    categoria=parametros['categoria'];
    latitud=parametros['latitud'];
    longitud=parametros['longitud'];
    altitud=parametros['altitud'];
    
    if usuario=="" or REGEX.match(usuario) or not esTipoValido(usuario,TIPO_CADENA):
        return False;
    if nombre=="" or REGEX.match(nombre) or not esTipoValido(nombre,TIPO_CADENA):
        return False;
    if categoria=="" or not esTipoValido(categoria,TIPO_ENTERO):
        return False;
    if latitud=="" or not esTipoValido(latitud,TIPO_FLOTANTE):
        return False;
    if longitud=="" or not esTipoValido(longitud,TIPO_FLOTANTE):
        return False;
    if altitud=="" or not esTipoValido(altitud,TIPO_FLOTANTE):
        return False;
    return True;

def sonParametrosObligatoriosActualizarPDIValidos(parametros):    
    usuario=parametros['usuario'];
    idPDI=parametros['idPDI'];    
    
    if usuario=="" or REGEX.match(usuario) or not esTipoValido(usuario,TIPO_CADENA):
        return False;
    if idPDI=="" or REGEX.match(idPDI) or not esTipoValido(idPDI,TIPO_ENTERO):
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
    if REGEX.match(paginaWeb) and not esURLValida(paginaWeb):
        return PDI_MENSAJE_URL_WEB_INVALIDA;
    if REGEX.match(telefono) and not esTipoValido(telefono,TIPO_ENTERO):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;
    if REGEX.match(email) and not esCorreoValido(email):
        return PDI_MENSAJE_CORREO_INVALIDO;
    if REGEX.match(urlImagen) and not esURLValida(urlImagen):
        return PDI_MENSAJE_URL_IMAGEN_INVALIDA;

    return True;

def registrarPuntoDeInteres(camposObligatorios):
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
                    guardarPuntoDeInteres(usuarioValido,posicionNueva,camposObligatorios,nuevoPDI);
                    
                    return CODIGO_REGISTRO_EXITOSO;    
                except Exception,err:
                    return CODIGO_CATEGORIA_INVALIDA;
            else:
                return CODIGO_LOCALIZACION_REPETIDA;
        else:
            return CODIGO_LIMITE_PDI_ALCANZADO;
    else:
        return CODIGO_USUARIO_INVALIDO;

def actualizarPuntoDeInteres(camposObligatorios,camposOpcionales):    
    usuarioValido=esUsuarioValido(camposObligatorios["usuario"]);
    if usuarioValido is not False:            
        pdi=PuntoDeInteres.objects.get(id=camposObligatorios["idPDI"]);
        
        #campos opcionales
        pdi.descripcion=camposOpcionales['descripcion'];
        pdi.direccion=camposOpcionales['direccion'];
        pdi.paginaWeb=camposOpcionales['paginaWeb'];
        pdi.telefono=camposOpcionales['telefono'];
        pdi.correoElectronico=camposOpcionales['email'];
        pdi.rutaImagen=camposOpcionales['imagen'];
    
        pdi.save();

        return CODIGO_REGISTRO_EXITOSO;    
    else:
        return CODIGO_USUARIO_INVALIDO;
    

def eliminarPuntoDeInteres(usuario,idPDI):
    validacion=esUsuarioValido(usuario);
    if validacion!=False:
        try:
            pdi=PuntoDeInteres.objects.get(pk=idPDI);
            #FALTA CODIGO DE ELIMINAR ANUNCIOS
            pdi.delete();
            return CODIGO_PDI_ELIMINADO;
        except Exception, err:
            return CODIGO_PDI_NO_EXISTE;
    else:        
        return CODIGO_USUARIO_INVALIDO;

def eliminarTodosPuntosDeInteresDeUsuario(usuario):
    listaPDI=obtenerPDIsDeUsuario(usuario);
    if(listaPDI==CODIGO_USUARIO_INVALIDO):
        return CODIGO_USUARIO_INVALIDO;
    if(len(listaPDI)>0):
        for pdi in listaPDI:
            idPDI=pdi.id;
            pdi.delete();      
        return CODIGO_PDI_ELIMINADO;
    else:
        return CODIGO_NO_HAY_PDIs_REGISTRADOS;
    
def guardarPuntoDeInteres(usuario,posicion,camposObligatorios,pdi):                    
    cat=Categoria.objects.get(pk=int(camposObligatorios["categoria"]))

    #campos obligatorios
    pdi.nombre=camposObligatorios["nombre"];
    pdi.categoria=cat;
    pdi.propietario=usuario;
    pdi.posicion=posicion;
    pdi.altitud=float(camposObligatorios['altitud']);  
    pdi.save();
    
    return;

def obtenerPDIsDeUsuario(usuario):
    usuarioValido=esUsuarioValido(usuario);
    if usuarioValido is not False: 
        listaPDI=PuntoDeInteres.objects.filter(propietario__email__exact=usuario);
        return listaPDI;
    else:    
        return CODIGO_USUARIO_INVALIDO;
    
    
    
    
    
