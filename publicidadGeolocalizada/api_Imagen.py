
"""
api_Anuncio.py: Se encarga de las funcionalidades asociadas
a anuncio, tales como registrar, modificar y eliminar uno
o todos los anuncios asociados a un PDI

@author Eric Huerta
@date 02/03/2013
"""

from publicidadGeolocalizada.models import *
from django.contrib.auth.models import User
from publicidadGeolocalizada.conversionTipos import *
from django.db import connection
from servidorPGPY.settings import MEDIA_ROOT
from servidorPGPY.settings import MEDIA_URL
from django.core.files.base import ContentFile
from PIL import Image
import imghdr
connection._rollback()

TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'

MAX_ANUNCIOS = 10
NO_HAY_ANUNCIOS = 0

CODIGO_REGISTRO_EXITOSO = 0
CODIGO_ELIMINAR_TODOS_EXITOSO = 0
CODIGO_REGISTRO_FALLIDO = 1
CODIGO_MODIFICA_FALLIDO = 1
CODIGO_ELIMINA_FALLIDO = 1

CODIGO_ID_ANUNCIO_INVALIDO = 2
CODIGO_ID_PDI_INVALIDO = 3
CODIGO_ID_USER_INVALIDO = 4
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

CODIGO_LIMITE_ANUNCIOS_ALCANZADO = 17
CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS = 18


def registrarImagen(imagen):
    
    tipoDeImagen = imghdr.what(imagen.imagen)
    
    if tipoDeImagen == 'jpeg':
    
        nuevaImagen = ImagenField()
        
    return imagen
    
    
    