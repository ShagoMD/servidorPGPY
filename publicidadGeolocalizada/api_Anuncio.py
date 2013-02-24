from publicidadGeolocalizada.models import *
from django.contrib.auth.models import User
from publicidadGeolocalizada.conversionTipos import *
from django.db import connection
connection._rollback()
#import pdb


def registrarAnuncio(idPDI,idUser,titulo,descripcion,categoria,URLimagen):
    
    parametrosObligatorios = sonParametrosObligatorios(idPDI,idUser,titulo,descripcion)
    parametrosOpcionales = sonParametrosOpcionales(categoria,URLimagen)
    
    PDIdelUsuario = esPDIdelUsuario(idPDI,idUser)

    if not PDIdelUsuario:
        return 1
    if not parametrosObligatorios:
        return 2
    
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
        return 3

def esPDIdelUsuario(idPDI,idUser):
    #pdb.set_trace()
    
    try:
        pdi = PuntoDeInteres.objects.get(id=idPDI)
    except Exception,err:
        print("No existe el PDI")
        return False
    
    id = pdi.propietario_id
    if id == int(float(idUser)):
        return True
    else:
        return False
    

def sonParametrosObligatorios(idPDI,idUser,titulo,descripcion):
    
    if idPDI==None and not esTipoValido(idPDI,TIPO_ENTERO):
        return False;
    if idUser==None and not esTipoValido(idUser,TIPO_ENTERO):
        return False;
    if titulo==None and not esTipoValido(titulo,TIPO_CADENA):
        return False;
    if descripcion==None and not esTipoValido(descripcion,TIPO_CADENA):
        return False;
    return True;

def sonParametrosOpcionales(categoria,URLimagen):
    
    if categoria!="" and not esTipoValido(categoria,TIPO_CADENA):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;
    if URLimagen!="" and not esTipoValido(URLimagen,TIPO_CADENA):
        return GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO;

    return True;

def validarParametros(idPDI,idUser,titulo,descripcion,categoria,URLimagen):
    parametrosValidos = True

    if idPDI == None and not esTipoValido(idPDI,TIPO_ENTERO):
       parametrosValidos = False
       
    elif idUser == None and not esTipoValido(idUser,TIPO_ENTERO):
        parametrosValidos = False
        
    elif titulo == None and not esTipoValido(titulo,TIPO_CADENA):    
         parametrosValidos = False
         
    elif descripcion == None and not esTipoValido(descripcion,TIPO_CADENA):
        parametrosValidos = False
        
    elif categoria == None and not esTipoValido(categoria,TIPO_CADENA):    
         parametrosValidos = False 
   
    elif URLimagen == None and not esTipoValido(URLimagen,TIPO_CADENA):
        parametrosValidos = False
        
    return parametrosValidos

