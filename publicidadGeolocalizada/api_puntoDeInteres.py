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
CARACTER_ESPACIO=re.compile('^\s+$');

CODIGO_REGISTRO_EXITOSO=0;

CODIGO_LOCALIZACION_REPETIDA=1;
CODIGO_LIMITE_PDI_ALCANZADO=2;
CODIGO_USUARIO_INVALIDO=3;
CODIGO_CATEGORIA_INVALIDA=4;
CODIGO_PDI_NO_EXISTE=5;
CODIGO_PDI_ELIMINADO=6;
CODIGO_NO_HAY_PDIs_REGISTRADOS=7;

CODIGO_PARAMETRO_USUARIO_INVALIDO=8;
CODIGO_PARAMETRO_PDI_INVALIDO=9;

CODIGO_ERROR_GUARDAR_PDI=10;
CODIGO_PDI_NO_PERTENECE_USUARIO=11;

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
    #pdb.set_trace()   
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

def sonParametrosObligatoriosRegistrarPDIValidos(parametros):
    usuario=parametros['usuario'];
    nombre=parametros['nombre'];
    categoria=parametros['categoria'];
    latitud=parametros['latitud'];
    longitud=parametros['longitud'];
    altitud=parametros['altitud'];
    

    if usuario=="" or CARACTER_ESPACIO.match(usuario) or not esTipoValido(usuario,TIPO_CADENA):
        return PDI_MENSAJE_PARAMETRO_USUARIO_INVALIDO;
    if nombre=="" or CARACTER_ESPACIO.match(nombre) or not esTipoValido(nombre,TIPO_CADENA):
        return PDI_MENSAJE_PARAMETRO_NOMBRE_PDI_INVALIDO;
    if categoria=="" or not esTipoValido(categoria,TIPO_ENTERO):
        return PDI_MENSAJE_PARAMETRO_CATEGORIA_INVALIDO;
    if latitud=="" or not esTipoValido(latitud,TIPO_FLOTANTE):
        return PDI_MENSAJE_PARAMETRO_LOCALIZACION_INVALIDO;
    if longitud=="" or not esTipoValido(longitud,TIPO_FLOTANTE):
        return PDI_MENSAJE_PARAMETRO_LOCALIZACION_INVALIDO;
    if altitud=="" or not esTipoValido(altitud,TIPO_FLOTANTE):
        return PDI_MENSAJE_PARAMETRO_LOCALIZACION_INVALIDO;
    return True;

def sonParametrosObligatoriosActualizarPDIValidos(parametros):    
    usuario=parametros['usuario'];
    idPDI=parametros['idPDI'];    
    
    if usuario=="" or CARACTER_ESPACIO.match(usuario) or not esTipoValido(usuario,TIPO_CADENA):
        return PDI_MENSAJE_PARAMETRO_USUARIO_INVALIDO;
    if idPDI=="" or CARACTER_ESPACIO.match(idPDI) or not esTipoValido(idPDI,TIPO_ENTERO):
        return PDI_MENSAJE_PARAMETRO_PDI_INVALIDO;
    return True;

def sonParametrosOpcionalesActualizarPDIValidos(parametros):
    descripcion=parametros["descripcion"];
    direccion=parametros["direccion"];
    paginaWeb=parametros["paginaWeb"];
    telefono=parametros["telefono"];
    email=parametros["email"];
    
    if CARACTER_ESPACIO.match(descripcion) or (descripcion!="" and not esTipoValido(descripcion,TIPO_CADENA)):
        return PDI_MENSAJE_PARAMETRO_DESCRIPCION_INVALIDO;
    if CARACTER_ESPACIO.match(direccion) or (direccion !="" and not esTipoValido(direccion,TIPO_CADENA)):
        return PDI_MENSAJE_PARAMETRO_DIRECCION_INVALIDO;
    if CARACTER_ESPACIO.match(paginaWeb) or (paginaWeb!="" and not esURLValida(paginaWeb)):
        return PDI_MENSAJE_PARAMETRO_URL_INVALIDO;
    if CARACTER_ESPACIO.match(telefono) or (telefono!="" and not esTipoValido(telefono,TIPO_ENTERO)):
        return PDI_MENSAJE_PARAMETRO_TELEFONO_INVALIDO;
    if CARACTER_ESPACIO.match(email) or (email!="" and not esCorreoValido(email)):
        return PDI_MENSAJE_PARAMETRO_CORREO_INVALIDO;

    return True;

def sonParametrosOpcionalesActualizarPDIVacios(parametros):    
    descripcion=parametros["descripcion"];
    direccion=parametros["direccion"];
    paginaWeb=parametros["paginaWeb"];
    telefono=parametros["telefono"];
    email=parametros["email"];    
    
    if CARACTER_ESPACIO.match(descripcion) or descripcion!="":
        return False;
    if CARACTER_ESPACIO.match(direccion) or direccion !="":
        return False;
    if CARACTER_ESPACIO.match(paginaWeb) or paginaWeb!="":
        return False;
    if CARACTER_ESPACIO.match(telefono) or telefono!="":
        return False;
    if CARACTER_ESPACIO.match(email) or email!="":
        return False;

    return True;

def registrarPuntoDeInteres(camposObligatorios):
    paramObligValidos=sonParametrosObligatoriosRegistrarPDIValidos(camposObligatorios);
    if paramObligValidos is not True:
        return paramObligValidos;
    
    usuarioValido=esUsuarioValido(camposObligatorios["usuario"]);
    if usuarioValido is False:
        return PDI_MENSAJE_USUARIO_INVALIDO;
                
    listaPDI=PuntoDeInteres.objects.filter(propietario__email__exact=camposObligatorios["usuario"]);
    if(len(listaPDI)>=MAXIMO_PDI_REGISTRADOS):
        return PDI_MENSAJE_LIMITE_PDI_ALCANZADO;
        
    posicionNueva=Point(float(camposObligatorios["longitud"]),float(camposObligatorios["latitud"]),srid=SRID);
    listaPDIPosiciones=PuntoDeInteres.objects.filter(posicion__exact=posicionNueva,altitud__exact=camposObligatorios['altitud']);
    if(len(listaPDIPosiciones)>0):
        return PDI_MENSAJE_LOCALIZACION_REPETIDA;
    
    try:
        cat=Categoria.objects.get(pk=int(camposObligatorios["categoria"]));
    except Exception,err:                
        return PDI_MENSAJE_CATEGORIA_INVALIDA;
               
    try:   
        nuevoPDI=PuntoDeInteres();
        guardarPuntoDeInteres(usuarioValido,posicionNueva,camposObligatorios,nuevoPDI);
        
        return CODIGO_REGISTRO_EXITOSO;    
    except Exception,err:
        return PDI_MENSAJE_REGISTRO_FALLIDO;


def actualizarPuntoDeInteres(camposObligatorios,camposOpcionales):
    paramObligValidos=sonParametrosObligatoriosActualizarPDIValidos(camposObligatorios);
    if paramObligValidos is not True:
        return paramObligValidos;
    
    paramOpcVacios=sonParametrosOpcionalesActualizarPDIVacios(camposOpcionales);
    paramOpcValidos=sonParametrosOpcionalesActualizarPDIValidos(camposOpcionales);
    if paramOpcVacios is not True and paramOpcValidos is not True:
            return paramOpcValidos;
    
    usuarioValido=esUsuarioValido(camposObligatorios["usuario"]);
    if usuarioValido is False:
        return PDI_MENSAJE_USUARIO_INVALIDO;
    
    listaPDI=PuntoDeInteres.objects.filter(id__exact=camposObligatorios["idPDI"],propietario__exact=usuarioValido.id);
    if(len(listaPDI)==0):        
        return PDI_MENSAJE_NO_PERTENECE_USUARIO;
    pdi=listaPDI[0];
    #campos opcionales
    pdi.descripcion=camposOpcionales['descripcion'];
    pdi.direccion=camposOpcionales['direccion'];
    pdi.paginaWeb=camposOpcionales['paginaWeb'];
    pdi.telefono=camposOpcionales['telefono'];
    pdi.correoElectronico=camposOpcionales['email'];

    try:
        pdi.save();
        return CODIGO_REGISTRO_EXITOSO;            
    except Exception,err:
        return PDI_MENSAJE_PDI_NO_ACTUALIZADO;

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
    
    
    
    
    
