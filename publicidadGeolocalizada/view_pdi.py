from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_puntoDeInteres import *

EVENT_FIELDS_BASIC = ["altitud","descripcion","latitud","longitud","nombre","paginaWeb","telefono"]
CAMPOS_LISTADO_PDI = ["longitud","latitud","rangoMaximoAlcance"]

def registrarPDI(request):
	if request.method == "POST":
		success, params = extract_params(request.POST,EVENT_FIELDS_BASIC)
		if success:
			return HttpResponse(params)
		else:			
			return HttpResponse(success)	
	else: 
		return render_to_response("PDI/registrar_poi.html", context_instance=RequestContext(request))
	
	
def obtenerListadoPuntosDeInteres(request):	
	if request.method == "POST":
		exito,parametros = extract_params(request.POST,CAMPOS_LISTADO_PDI)
		if exito:
			obtenerListadoPuntosDeInteres(parametros['latitud'],parametros['longitud'],parametros['rangoMaximoAlcance'])
			return HttpResponse(exito)
		else:
			return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros de la peticion son incorrectos'})
	else:
		return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
		
				