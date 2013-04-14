
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

def registrarImagen(imagen, correo):
    
    tipoDeImagen = imghdr.what(imagen.imagen)
    
    if tipoDeImagen == 'jpeg' :
        
        #listaDeImagenes = ImagenField.objects.all()
        #for eliminarImagen in listaDeImagenes:
        #    eliminarImagen.delete()  
        
        try:
            usuario = User.objects.get(email=correo)
        except User.DoesNotExist:
            return CODIGO_USUARIO_NO_EXISTE
        
        #nombre = imagen.imagen.name
        nombreImagen = correo+'.jpeg'
        url = imagen.imagen.url
        
        if len(nombreImagen) >= 100:
            return CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO
        
        try:
            antiguaImagen = ImagenField.objects.get(nombre=nombreImagen)
        except Exception,err:
            imagen.nombre = nombreImagen
            fh = ContentFile(imagen.imagen.read())
            imagen.imagen.save(nombreImagen, fh)
            imagen.urlImagen = url
            imagen.save()
            
            return imagen
        
        antiguaImagen.imagen.delete()
        antiguaImagen.delete()
        
        imagen.nombre = nombreImagen
        fh = ContentFile(imagen.imagen.read())
        imagen.imagen.save(nombreImagen, fh)
        imagen.urlImagen = url
        imagen.save()
        
        return imagen
        
    return CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO
    
    
    
