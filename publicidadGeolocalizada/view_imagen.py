
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

CAMPOS_IMAGEN = ["imagen"]
CAMPOS_SEARCH = ["idImagen"]

def peticionImagen(request):
	if request.method == "POST":
        
		form = UploadFileForm(request.POST, request.FILES)
        
		if not form.is_valid():
		
			imagen = ImagenField()
			
			#file = params[0]
			#size = (50,50)
			imagen.imagen = request.FILES['imagen']
			
			nombre = imagen.imagen.name
			url = imagen.imagen.url
			
			imagen.nombre = nombre
			imagen.urlImagen = url
	
			fh = ContentFile(imagen.imagen.read())
			#fh._set_size(500)
			imagen.imagen.save(nombre, fh)
			#i.file
			#imghdr.what("/home/user/Pictures/Foto2x2.jpg")
			imagen.save()
			#imghdr.what(imagen.imagen)
			
			return render_to_response("PDI/respuesta/error.json",{'codigo':100, 'mensaje': request.build_absolute_uri('/geoAdds'+imagen.imagen.url) })
		
		else:
			return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El campo de imagen se encuentra vacio'})

	else: 
		return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})

def peticionObtenerURL(request):
	if request.method == "POST":
		
		params = extract_params(request.POST,CAMPOS_SEARCH)
		
		idImag = 2
		
		imagen = ImagenField()
		
		imagen = ImagenField.objects.get(id=idImag)
		
		return render_to_response("PDI/respuesta/error.json",{'codigo':100, 'mensaje': request.build_absolute_uri('/geoAdds'+imagen.imagen.url) })
		
	else:
		return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
	
class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file  = forms.FileField()
    
    def process(self):
        cd = self.cleaned_data
        
        