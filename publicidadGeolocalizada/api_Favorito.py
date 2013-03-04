from publicidadGeolocalizada.models import *
from django.contrib.auth.models import User
from publicidadGeolocalizada.conversionTipos import *
from django.db import connection
connection._rollback()

TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'

CODIGO_MARCACION_EXITOSO = 0
CODIGO_DESMARCACION_EXITOSO = 0
CODIGO_MARCACION_FALLIDO = 1
CODIGO_DESMARCACION_FALLIDO = 1

CODIGO_ID_PDI_INVALIDO = 2
CODIGO_ID_USER_INVALIDO = 3

CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS = 4

CODIGO_EXISTE_PDI = 5
CODIGO_NO_EXISTE_PDI = 6
CODIGO_EXISTE_USER = 7
CODIGO_NO_EXISTE_USER = 8

CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO = 9
CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO = 10

def marcarPDIcomoFavorito(idPDI,idUser):
    
    parametrosObligatorios = sonParametrosObligatorios(idPDI,idUser)

    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    existePDI = verificarPDI(idPDI)
    existeUser = verificarUser(idUser)
    
    if existePDI != CODIGO_EXISTE_PDI:
        return existePDI
    if existeUser != CODIGO_EXISTE_USER:
        return existeUser
    
    #yaSeEncuentraMarcado = verificarSiEstaMarcado(idPDI, idUser)
    
    #if yaSeEncuentraMarcado != CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO:
    #    return CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO
    
    try:
        
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        usuario = User.objects.get(id=idUser)         
        
        pdi.favoritos.add(usuario)
         
        return CODIGO_MARCACION_EXITOSO
    
    except Exception,err:
        return CODIGO_MARCACION_FALLIDO
    

def desmarcarPDIcomoFavorito(idPDI,idUser):
    
    parametrosObligatorios = sonParametrosObligatorios(idPDI,idUser)

    if parametrosObligatorios != CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS:
        return parametrosObligatorios
    
    existePDI = verificarPDI(idPDI)
    existeUser = verificarUser(idUser)
    
    if existePDI != CODIGO_EXISTE_PDI:
        return existePDI
    if existeUser != CODIGO_EXISTE_USER:
        return existeUser
    
    #seEncuentraMarcado = verificarSiEstaMarcado(idPDI, idUser)
    
    #if seEncuentraMarcado != CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO:
    #    return CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO
    
    try:
        
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        usuario = User.objects.get(id=idUser)         
        
        pdi.favoritos.remove(usuario)
         
        return CODIGO_DESMARCACION_EXITOSO
    
    except Exception,err:
        return CODIGO_DESMARCACION_FALLIDO


def verificarPDI(idPDI):
    
    try:
        pdi = PuntoDeInteres.objects.get(id=idPDI)
        return CODIGO_EXISTE_PDI
    except Exception,err:
        return CODIGO_NO_EXISTE_PDI
    

def verificarUser(idUser):
    
    try:
        usuario = User.objects.get(id=idUser)
        return CODIGO_EXISTE_USER
    except Exception,err:
        return CODIGO_NO_EXISTE_USER
    
def verificarSiEstaMarcado(idPDI, idUser):
    
    try:
        listaDePDIFavoritos = PuntoDeInteres.objects.filter(favoritos__id__exact = idUser)
        
        if(len(listaDeUsuariosFavoritos)==0):
            return CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO
        
        for pdi in listaDePDIFavoritos:
            id_PDI = pdi.id
            if(id_PDI == int(float(inPDI))):
                return CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO
            
        return CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO
    except Exception,err:
        return CODIGO_NO_EXISTE_PDI

def sonParametrosObligatorios(idPDI,idUser):
    
    if len(idPDI)==0 or not esTipoValido(idPDI,TIPO_ENTERO):
        return CODIGO_ID_PDI_INVALIDO
    if len(idUser)==0 or not esTipoValido(idUser,TIPO_ENTERO):
        return CODIGO_ID_USER_INVALIDO
    
    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS

