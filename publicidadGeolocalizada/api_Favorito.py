
"""
api_Favorito.py: Se encarga de las funcionalidades asociadas
a marcar y desmarcar un PDI como favorito de parte de un usuario

@author Eric Huerta
@date 03/03/2013
"""

from models import *
from django.contrib.auth.models import User
from conversionTipos import *
from django.db import connection
connection._rollback()

TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'

CODIGO_MARCAR_PDI = 0
CODIGO_DESMARCAR_PDI = 1

CODIGO_MARCACION_EXITOSO = 0
CODIGO_DESMARCACION_EXITOSO = 0
CODIGO_MARCACION_FALLIDO = 1
CODIGO_DESMARCACION_FALLIDO = 1

CODIGO_ID_PDI_INVALIDO = 2
CODIGO_CORREO_USER_INVALIDO = 3
CODIGO_MARCADO_INVAIDO = 4
CODIGO_NOTIFICACIONES_INVALIDO = 5

CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS = 6

CODIGO_EXISTE_PDI = 7
CODIGO_NO_EXISTE_PDI = 8
CODIGO_EXISTE_USER = 9
CODIGO_NO_EXISTE_USER = 10

CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO = 11
CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO = 12

CODIGO_DE_OPCIONES_DE_MARCADO_INCORRECTO = 13

def marcarPDIcomoFavorito(idPDI,correo_e,marcado):
    
    parametrosObligatorios = sonParametrosObligatoriosMarcacion(idPDI,correo_e,marcado)
    
    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    if int(float(marcado)) != 0 and int(float(marcado)) != 1:
        return CODIGO_DE_OPCIONES_DE_MARCADO_INCORRECTO
    
    existePDI = verificarPDI(idPDI)
    existeUser = verificarUser(correo_e)
    
    if existePDI != CODIGO_EXISTE_PDI:
        return existePDI
    if existeUser != CODIGO_EXISTE_USER:
        return existeUser
    
    if int(float(marcado)) == 1:
        desmarcacionExitosa = desmarcarPDIcomoFavorito(idPDI,correo_e)
        return desmarcacionExitosa
    
    yaSeEncuentraMarcado = verificarSiEstaMarcado(idPDI, correo_e)
    
    if yaSeEncuentraMarcado != CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO:
        return CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO
    
    try:
        
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        usuario = User.objects.get(email=correo_e)         
        
        pdi.favoritos.add(usuario)
         
        return pdi
    
    except Exception,err:
        return CODIGO_MARCACION_FALLIDO
    

def desmarcarPDIcomoFavorito(idPDI,correo_e):
    
    
    seEncuentraMarcado = verificarSiEstaMarcado(idPDI, correo_e)
    
    if seEncuentraMarcado != CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO:
        return CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO
    
    try:
        
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        usuario = User.objects.get(email=correo_e)         
        
        pdi.favoritos.remove(usuario)
         
        return pdi
    
    except Exception,err:
        return CODIGO_DESMARCACION_FALLIDO


def verificarPDI(idPDI):
    
    try:
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        return CODIGO_EXISTE_PDI
    except Exception,err:
        return CODIGO_NO_EXISTE_PDI
    

def verificarUser(correo_e):
    
    try:
        usuario = User.objects.get(email=correo_e)
        return CODIGO_EXISTE_USER
    except Exception,err:
        return CODIGO_NO_EXISTE_USER

def verficaCorreo(correoUsuario):
    
    try:
        usuario = User.objects.get(email=correoUsuario)
        return CODIGO_EXISTE_USER
    except Exception,err:
        return CODIGO_NO_EXISTE_USER
    
def verificarSiEstaMarcado(idPDI, correo_e):
    
    try:
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        
        listaDePDIFavoritos = pdi.favoritos.filter(email__exact = correo_e)
        
        if(len(listaDePDIFavoritos)==0):
            return CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO
        
        return CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO

    except Exception,err:
        return CODIGO_NO_EXISTE_PDI

def sonParametrosObligatoriosMarcacion(idPDI,correo_e,marcado):
    
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO
    if len(correo_e)==0 or not esTipoValido(correo_e,TIPO_CADENA):
        return CODIGO_CORREO_USER_INVALIDO
    if len(marcado)==0 or not esTipoValido(marcado,TIPO_ENTERO):
        return CODIGO_MARCADO_INVAIDO
    
    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

