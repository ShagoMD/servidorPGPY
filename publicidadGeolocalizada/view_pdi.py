from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import extract_params, _extract_params
from django.template import RequestContext

EVENT_FIELDS_BASIC = ["altitud","descripcion","latitud","longitud","nombre","paginaWeb","telefono"]


def registrarPDI(request):
	if request.method == "POST":
		success, params = extract_params(request.POST,EVENT_FIELDS_BASIC)
		if success:
			return HttpResponse(params)
		else:			
			return HttpResponse(success)	
	else: 
		return render_to_response("PDI/registrar_poi.html", context_instance=RequestContext(request))