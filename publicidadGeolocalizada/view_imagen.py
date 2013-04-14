
"""
view_imagen.py: Se encarga de la funcionalidad de
subir una imagen al servidor

@author Eric Huerta
@date 01/03/2013
"""

from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from servidorPGPY.settings import MEDIA_ROOT
from servidorPGPY.settings import MEDIA_URL
from models import *
from django.core.files.base import ContentFile
from PIL import Image
from api_Imagen import *
import imghdr
from django import forms

CAMPOS_IMAGEN = ["correo"]
CAMPOS_SEARCH = ["idImagen"]

def peticionImagen(request):
	if request.method == "POST":
		
		success, parametrosPeticion = extract_params(request.POST,CAMPOS_IMAGEN)
		
		if success:
			
			imagen = ImagenField()
	
			try:
				imagen.imagen = request.FILES['imagen']
				nueva = registrarImagen(imagen, parametrosPeticion["correo"])
				#nombre = imagen.imagen.name
				#url = imagen.imagen.url
				
				#imagen.nombre = nombre
				#imagen.urlImagen = url
		
				#fh = ContentFile(imagen.imagen.read())
				#imagen.imagen.save(nombre, fh)
				#imagen.save()
				
				if nueva == CODIGO_IMAGEN_NO_ES_DEL_TIPO_VALIDO:
					return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La imagen no es un jpeg.'})
				if nueva == CODIGO_NOMBRE_DE_IMAGEN_MUY_LARGO:
					return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El nombre de la imagen es mayor que 100 caracteres.'})
				if nueva == CODIGO_USUARIO_NO_EXISTE:
					return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El usuario no existe.'})
				
				return render_to_response("PDI/respuesta/error.json",{'codigo':100, 'mensaje': request.build_absolute_uri('/geoAdds'+imagen.imagen.url) })
				
			except KeyError:
				return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El campo de imagen se encuentra vacio'})
		else:
			return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros son incorrectos'})
	else: 
		return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})

	

        
        