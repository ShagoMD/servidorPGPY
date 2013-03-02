from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from servidorPGPY.settings import MEDIA_ROOT
from models import *
from django.core.files.base import ContentFile
from PIL import Image

#CAMPOS_IMAGEN = ["nombre", "imagen"]
CAMPOS_IMAGEN = ["imagen"]

def peticionImagen(request):
	if request.method == "POST":
		params = extract_params(request.POST,CAMPOS_IMAGEN)
       
		#if success:
			
		imagen = Imagen()
		
		#file = params[0]
		#size = (50,50)
		imagen.imagen = request.FILES['imagen']
		
		nombre = imagen.imagen.name

		fh = ContentFile(imagen.imagen.read())
		#fh._set_size(500)
		imagen.imagen.save(nombre, fh)
		#i.file
		
		#archivo.save();
		
		#fd = open('%s/%s' % (MEDIA_ROOT, file[0]), 'wb')
		#fd.write(file[2])
		#fd.close()
		
		return render_to_response("PDI/respuesta/error.json",{'codigo':100, 'mensaje':'Exito, imagen :'})
		#else:			
		#	return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Parametros incorrectos'})	
	else: 
		return render_to_response("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
