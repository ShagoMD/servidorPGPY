from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_puntoDeInteres import *

EVENT_FIELDS_BASIC = ["altitud","descripcion","latitud","longitud","nombre","paginaWeb","telefono"]
CAMPOS_LISTADO_PDI = ["latitud","longitud","rangoMaximoAlcance","searchString"]

def peticionObtenerListadoPuntosDeInteresSearch(request):	
	if request.method == "POST":
		
		
		success, parametrosPeticion = extract_params(request.POST,CAMPOS_LISTADO_PDI)
       
		if success:
			
			try:	
				
				lista_puntos_de_interes = obtenerListadoPuntosDeInteresSearch(parametrosPeticion["latitud"],parametrosPeticion["longitud"],parametrosPeticion["rangoMaximoAlcance"],parametrosPeticion["searchString"])
				return	render_to_json("PDI/respuesta/puntoDeInteres.json",{'codigo':100, 'lista_pdi':lista_puntos_de_interes})
			except Exception,err:
				   
				   return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err})
					
		else:			
			
			return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros son incorrectos'})
	else:
		
		return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
		
				


