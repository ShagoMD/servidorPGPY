
"""
api_Anuncio.py: Se encarga de las funcionalidades asociadas
a anuncio, tales como registrar, modificar y eliminar uno
o todos los anuncios asociados a un PDI

@author Eric Huerta
@date 02/03/2013
"""

from models import *
from django.contrib.auth.models import User
from conversionTipos import *
from django.db import connection
from servidorPGPY.settings import MEDIA_ROOT
from servidorPGPY.settings import MEDIA_URL
from django.core.files.base import ContentFile
from PIL import Image
import imghdr
connection._rollback()

CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO = 0
CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO = 1
CODIGO_USUARIO_NO_EXISTE = 2
CODIGO_PDI_NO_EXISTE = 2
CODIGO_ANUNCIO_NO_EXISTE = 2

def registrarImagenUsuario(imagen, correo):
    
    tipoDeImagen = imghdr.what(imagen.imagen)
    
    if tipoDeImagen == 'jpeg' or tipoDeImagen == 'jpg' or tipoDeImagen =='png':
        
        try:
            usuario = User.objects.get(email=correo)
        except User.DoesNotExist:
            if correo == 'pgpy':
                nombre = imagen.imagen.name
                url = imagen.imagen.url
                
                imagen.nombre = nombre
                imagen.urlImagen = url
        
                fh = ContentFile(imagen.imagen.read())
                imagen.imagen.save(nombre, fh)
                imagen.save()
                
                return imagen
            return CODIGO_USUARIO_NO_EXISTE
        
        #nombre = imagen.imagen.name
        nombreImagen = correo+'.jpeg'
        #url = imagen.imagen.url
        
        if len(nombreImagen) >= 100:
            return CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO
        
        try:
            antiguaImagen = ImagenField.objects.get(nombre=nombreImagen)
        except Exception,err:
            imagen.nombre = nombreImagen
            fh = ContentFile(imagen.imagen.read())
            imagen.imagen.save(nombreImagen, fh)
            imagen.urlImagen = imagen.imagen.url
            imagen.save()
            
            return imagen
        
        antiguaImagen.imagen.delete()
        antiguaImagen.delete()
        
        imagen.nombre = nombreImagen
        fh = ContentFile(imagen.imagen.read())
        imagen.imagen.save(nombreImagen, fh)
        imagen.urlImagen = imagen.imagen.url
        imagen.save()
        
        return imagen
        
    return CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO
    
    
def registrarImagenPDI(imagen, idPDI):
    
    tipoDeImagen = imghdr.what(imagen.imagen)
    
    if tipoDeImagen == 'jpeg' or tipoDeImagen == 'jpg' or tipoDeImagen =='png':  
        
        try:
            pdi = PuntoDeInteres.objects.get(id=idPDI)
        except Exception,err:
            return CODIGO_PDI_NO_EXISTE
        
        #nombre = imagen.imagen.name
        nombreImagen = idPDI+'-pdi.jpeg'
        #url = imagen.imagen.url
        
        if len(nombreImagen) >= 100:
            return CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO
        
        try:
            antiguaImagen = ImagenField.objects.get(nombre=nombreImagen)
        except Exception,err:
            imagen.nombre = nombreImagen
            fh = ContentFile(imagen.imagen.read())
            imagen.imagen.save(nombreImagen, fh)
            imagen.urlImagen = imagen.imagen.url
            imagen.save()
            
            return imagen
        
        antiguaImagen.imagen.delete()
        antiguaImagen.delete()
        
        imagen.nombre = nombreImagen
        fh = ContentFile(imagen.imagen.read())
        imagen.imagen.save(nombreImagen, fh)
        imagen.urlImagen = imagen.imagen.url
        imagen.save()
        
        return imagen
        
    return CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO    
    
def registrarImagenAnuncio(imagen, idAnuncio):
    
    tipoDeImagen = imghdr.what(imagen.imagen)
    
    if tipoDeImagen == 'jpeg' or tipoDeImagen == 'jpg' or tipoDeImagen =='png':
        
        try:
            anuncio = Anuncio.objects.get(id=idAnuncio)
        except Exception,err:
            return CODIGO_ANUNCIO_NO_EXISTE
        
        #nombre = imagen.imagen.name
        nombreImagen = idAnuncio+'-anuncio.jpeg'
        #url = imagen.imagen.url
        
        if len(nombreImagen) >= 100:
            return CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO
        
        try:
            antiguaImagen = ImagenField.objects.get(nombre=nombreImagen)
        except Exception,err:
            imagen.nombre = nombreImagen
            fh = ContentFile(imagen.imagen.read())
            imagen.imagen.save(nombreImagen, fh)
            imagen.urlImagen = imagen.imagen.url
            imagen.save()
            
            return imagen
        
        antiguaImagen.imagen.delete()
        antiguaImagen.delete()
        
        imagen.nombre = nombreImagen
        fh = ContentFile(imagen.imagen.read())
        imagen.imagen.save(nombreImagen, fh)
        imagen.urlImagen = imagen.imagen.url
        imagen.save()
        
        return imagen
        
    return CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO

def eliminarTodo():
    try:
        listaDeImagenes = ImagenField.objects.all()
        for imagen in listaDeImagenes:
            imagen.imagen.delete()
            imagen.delete()  
        return
    except Exception,err:
        return
    return