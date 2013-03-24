
"""
api_Anuncio.py: Se encarga de las funcionalidades asociadas
a anuncio, tales como registrar, modificar y eliminar uno
o todos los anuncios asociados a un PDI

@author Eric Huerta
@date 02/03/2013
"""

from models import *
from conversionTipos import *
from django.contrib.auth.models import User
from django.db import connection
from utilidades import *
connection._rollback()
#import pdb

TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'

MAX_ANUNCIOS = 10
NO_HAY_ANUNCIOS = 0

CODIGO_REGISTRO_EXITOSO = 0
CODIGO_ELIMINAR_TODOS_EXITOSO = 0
CODIGO_ELIMINAR_EXITOSO = 0
CODIGO_OBTENER_TODOS_LOS_ANUNCIOS_EXITOSO = 0
CODIGO_REGISTRO_FALLIDO = 1
CODIGO_MODIFICA_FALLIDO = 1
CODIGO_ELIMINA_FALLIDO = 1
CODIGO_OBTENER_TODOS_LOS_ANUNCIOS_FALLIDO = 1

CODIGO_ID_ANUNCIO_INVALIDO = 2
CODIGO_ID_PDI_INVALIDO = 3
CODIGO_CORREO_USER_INVALIDO = 4
CODIGO_TITULO_ANUNCIO_INVALIDO = 5
CODIGO_DESCRIPCION_ANUNCIO_INVALIDO = 6
CODIGO_CATEGORIA_ANUNCIO_INVALIDO = 7
CODIGO_URL_IMAGEN_ANUNCIO_INVALIDO = 8

CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS = 9
CODIGO_PARAMETROS_OPCIONALES_VALIDOS = 10

CODIGO_ANUNCIO_NO_ES_DEL_PDI = 11
CODIGO_ANUNCIO_ES_DEL_PDI = 12
CODIGO_PDI_NO_ES_DEL_USUARIO = 13
CODIGO_PDI_ES_DEL_USUARIO = 14

CODIGO_PDI_NO_EXISTE = 15
CODIGO_ANUNCIO_NO_EXISTE = 16
CODIGO_USER_NO_EXISTE = 17

CODIGO_LIMITE_ANUNCIOS_ALCANZADO = 18
CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS = 19



def registrarAnuncio(idPDI,correo_e,titulo,descripcion,categoria,URLimagen):
    
    parametrosObligatorios = sonParametrosObligatorios(idPDI,correo_e,titulo,descripcion,categoria)
    parametrosOpcionales = sonParametrosOpcionales(URLimagen)

    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    if parametrosOpcionales != CODIGO_PARAMETROS_OPCIONALES_VALIDOS:
        return parametrosOpcionales
    
    PDIdelUsuario = esPDIdelUsuario(idPDI,correo_e)
    totalDeAnuncios = obtenerElTotalDeAnunciosDelPDI(idPDI)

    if PDIdelUsuario != CODIGO_PDI_ES_DEL_USUARIO:
        return PDIdelUsuario
    

    if(len(totalDeAnuncios) >= MAX_ANUNCIOS):
        return CODIGO_LIMITE_ANUNCIOS_ALCANZADO
    
    try:
        
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        nuevoAnuncio = Anuncio()
        nuevoAnuncio.anunciante = pdi
        nuevoAnuncio.titulo = titulo
        nuevoAnuncio.descripcion = descripcion
        nuevoAnuncio.categoria = categoria
        nuevoAnuncio.rutaImagen = URLimagen
        nuevoAnuncio.save()            
        return nuevoAnuncio
    
    except Exception,err:
        return CODIGO_REGISTRO_FALLIDO

def modificarAnuncio(idAnuncio,idPDI,correo_e,titulo,descripcion,categoria,URLimagen):
    
    parametrosObligatorios = sonParametrosObligatoriosCambio(idAnuncio,idPDI,correo_e,titulo,descripcion,categoria)
    parametrosOpcionales = sonParametrosOpcionales(URLimagen)
    
    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    if parametrosOpcionales != CODIGO_PARAMETROS_OPCIONALES_VALIDOS:
        return parametrosOpcionales
    
    
    PDIdelUsuario = esPDIdelUsuario(idPDI,correo_e)
    totalDeAnuncios = obtenerElTotalDeAnunciosDelPDI(idPDI)
    
    if PDIdelUsuario != CODIGO_PDI_ES_DEL_USUARIO:
        return PDIdelUsuario
    
    if (len(totalDeAnuncios) == NO_HAY_ANUNCIOS): 
        return CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS
    
    AnunciodePDI = esAnunciodelPDI(idAnuncio,idPDI)
    
    if AnunciodePDI != CODIGO_ANUNCIO_ES_DEL_PDI:
        return AnunciodePDI
    
    try:
        
        anuncio = Anuncio.objects.get(id=idAnuncio)
        anuncio.titulo = titulo
        anuncio.descripcion = descripcion
        anuncio.categoria = categoria
        anuncio.rutaImagen = URLimagen
        anuncio.save()  
        return anuncio
    
    except Exception,err:
        return CODIGO_MODIFICA_FALLIDO

def eliminarAnuncio(idAnuncio,idPDI,correo_e):
    
    parametrosObligatorios = sonParametrosObligatoriosEliminar(idAnuncio,idPDI,correo_e)
    
    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    PDIdelUsuario = esPDIdelUsuario(idPDI,correo_e)
    totalDeAnuncios = obtenerElTotalDeAnunciosDelPDI(idPDI)
    
    if PDIdelUsuario != CODIGO_PDI_ES_DEL_USUARIO:
        return PDIdelUsuario
    
    if (len(totalDeAnuncios) == NO_HAY_ANUNCIOS): 
        return CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS
    
    AnunciodePDI = esAnunciodelPDI(idAnuncio,idPDI)
    
    if AnunciodePDI != CODIGO_ANUNCIO_ES_DEL_PDI:
        return AnunciodePDI
    
    try:
        
        anuncio = Anuncio.objects.get(id=idAnuncio)
        anuncio.delete()  
        return CODIGO_ELIMINAR_EXITOSO
    
    except Exception,err:
        return CODIGO_ELIMINA_FALLIDO

def eliminarTodosLosAnuncios(idPDI,correo_e):
    
    parametrosObligatorios = sonParametrosObligatoriosEliminar(idAnuncio,idPDI,correo_e)
    
    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    PDIdelUsuario = esPDIdelUsuario(idPDI,correo_e)
    totalDeAnuncios = obtenerElTotalDeAnunciosDelPDI(idPDI)
    
    if PDIdelUsuario != CODIGO_PDI_ES_DEL_USUARIO:
        return PDIdelUsuario
    
    if (len(totalDeAnuncios) == NO_HAY_ANUNCIOS): 
        return CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS
    
    try:
        
        for anuncio in totalDeAnuncios:
            idAnuncio = anuncio.id
            anuncio.delete()  
        return CODIGO_ELIMINAR_TODOS_EXITOSO
    
    except Exception,err:
        return CODIGO_ELIMINA_FALLIDO

def obtenerTodosLosAnunciosDelPDI(idPDI):
    
    parametrosObligatorios = sonParametrosObligatoriosTodosLosAnuncios(idPDI)
    
    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    totalDeAnuncios = obtenerElTotalDeAnunciosDelPDI(idPDI)
    
    if (len(totalDeAnuncios) == NO_HAY_ANUNCIOS): 
        return CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS

    return totalDeAnuncios

def esPDIdelUsuario(idPDI,correo_e):
    
    try:
        pdi = PuntoDeInteres.objects.get(id=idPDI)
    except Exception,err:
        return CODIGO_PDI_NO_EXISTE
    
    idUser = pdi.propietario_id
    
    try:
        usuario = User.objects.get(id=idUser)
    except Exception,err:
        return CODIGO_USER_NO_EXISTE
    
    if correo_e == usuario.email:
        return CODIGO_PDI_ES_DEL_USUARIO
    else:
        return CODIGO_PDI_NO_ES_DEL_USUARIO

def esAnunciodelPDI(idAnuncio,idPDI):
    
    try:
        anuncio = Anuncio.objects.get(id=idAnuncio)
    except Exception,err:
        return CODIGO_ANUNCIO_NO_EXISTE

    id = anuncio.anunciante_id
    if id == int(float(idPDI)):
        return CODIGO_ANUNCIO_ES_DEL_PDI
    else:
        return CODIGO_ANUNCIO_NO_ES_DEL_PDI    

def obtenerElTotalDeAnunciosDelPDI(idPDI):
    
    listaDeAnuncios = Anuncio.objects.filter(anunciante=idPDI);
    
    return listaDeAnuncios


def sonParametrosObligatorios(idPDI,idUser,titulo,descripcion,categoria):
    
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO
    if len(idUser)==0 or not esTipoValido(idUser,TIPO_CADENA):
        return CODIGO_CORREO_USER_INVALIDO
    if len(titulo)==0 or not esTipoValido(titulo,TIPO_CADENA):
        return CODIGO_TITULO_ANUNCIO_INVALIDO
    if len(descripcion)==0 or not esTipoValido(descripcion,TIPO_CADENA):
        return CODIGO_DESCRIPCION_ANUNCIO_INVALIDO
    if len(categoria)==0 or not esTipoValido(categoria,TIPO_CADENA):
        return CODIGO_CATEGORIA_ANUNCIO_INVALIDO

    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

def sonParametrosObligatoriosTodosLosAnuncios(idPDI):
    
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO

    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

def sonParametrosObligatoriosCambio(idAnuncio,idPDI,correo_e,titulo,descripcion,categoria):
    
    if len(idAnuncio)==0 or not esTipoValido(idAnuncio,TIPO_ENTERO):
        return CODIGO_ID_ANUNCIO_INVALIDO
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO
    if len(correo_e)==0 or not esTipoValido(correo_e,TIPO_CADENA):
        return CODIGO_CORREO_USER_INVALIDO
    if len(titulo)==0 or not esTipoValido(titulo,TIPO_CADENA):
        return CODIGO_TITULO_ANUNCIO_INVALIDO
    if len(descripcion)==0 or not esTipoValido(descripcion,TIPO_CADENA):
        return CODIGO_DESCRIPCION_ANUNCIO_INVALIDO
    if len(categoria)==0 or not esTipoValido(categoria,TIPO_CADENA):
        return CODIGO_CATEGORIA_ANUNCIO_INVALIDO
    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

def sonParametrosObligatoriosEliminar(idAnuncio,idPDI,correo_e):
    
    if len(idAnuncio)==0 or not esTipoValido(idAnuncio,TIPO_ENTERO):
        return CODIGO_ID_ANUNCIO_INVALIDO
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO
    if len(correo_e)==0 or not esTipoValido(correo_e,TIPO_CADENA):
        return CODIGO_CORREO_USER_INVALIDO
    
    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

def sonParametrosOpcionales(URLimagen):
    
    if not esTipoValido(URLimagen,TIPO_CADENA):
        return CODIGO_URL_IMAGEN_ANUNCIO_INVALIDO

    return CODIGO_PARAMETROS_OPCIONALES_VALIDOS
