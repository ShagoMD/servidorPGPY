from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_puntoDeInteres import *

EVENT_FIELDS_BASIC = ["altitud","descripcion","latitud","longitud","nombre","paginaWeb","telefono"]
CAMPOS_LISTADO_PDI = ["latitud","longitud","rangoMaximoAlcance","searchString","categoria"]

def registrarPDI(request):
	if request.method == "POST":
		success, params = extract_params(request.POST,EVENT_FIELDS_BASIC)
       
		if success:
			return HttpResponse(params)
		else:			
			return HttpResponse(params)	
	else: 
		return render_to_response("PDI/registrar_poi.html", context_instance=RequestContext(request))
	
	
def peticionObtenerListadoPuntosDeInteresSearchCategoria(request):	
	if request.method == "POST":
		
		
		success, parametrosPeticion = extract_params(request.POST,CAMPOS_LISTADO_PDI)
       
		if success:
			try:	
				
				lista_puntos_de_interes = obtenerListadoPuntosDeInteresSearchCategoria(parametrosPeticion["latitud"],parametrosPeticion["longitud"],parametrosPeticion["rangoMaximoAlcance"],parametrosPeticion["searchString"],parametrosPeticion["categoria"])
				return	render_to_json("PDI/respuesta/puntoDeInteres.json",{'codigo':100, 'lista_pdi':lista_puntos_de_interes})
			except Exception,err:
				   
				   return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err})
					
		else:			
			
			return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros son incorrectos'})
	else:
		
		return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
		
				
				

