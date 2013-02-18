from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_puntoDeInteres import *

CAMPOS_OBLIGATORIOS_REGISTRO_PDI = ["usuario","latitud","longitud","nombre","categoria"]
CAMPOS_OPCIONALES_REGISTRO_PDI=["descripcion","direccion","paginaWeb","telefono","email","imagen"]

CAMPOS_LISTADO_PDI = ["latitud","longitud","rangoMaximoAlcance"]

def registrarPDI(request):
	if request.method == "POST":
		success, paramObligatorios = extract_params(request.POST,CAMPOS_OBLIGATORIOS_REGISTRO_PDI)
		success2,paramOpcionales=extract_params(request.POST,CAMPOS_OPCIONALES_REGISTRO_PDI)
       
		if success:
			exito=registrarPuntoDeInteres(CAMPOS_OBLIGATORIOS_REGISTRO_PDI,CAMPOS_OPCIONALES_REGISTRO_PDI);
			if(exito==0):
				return render_to_json("PDI/respuesta/registroPDI.json",{'codigo':100,'mensaje':'Registro de PDI exitoso'});
			if(exito==1):
				return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':'Los datos de localizacion del PDI que se desea registrar ya han sido utilizados previamente.'});
			if(exito==2):
				return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':'Se ha alcanzado el limite de PDI que su cuenta le permite registrar.'});
			if(exito==3):
				return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':'El usuario que intenta registrar el PDI no existe.'});
		else:	
			return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':'No se enviaron todos los parametros obligatorios.'});						
	else:
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':'La peticion no fue realizada a traves de POST.'});		
	
def peticionObtenerListadoPuntosDeInteres(request):	
	if request.method == "POST":
		
		
		success, parametrosPeticion = extract_params(request.POST,CAMPOS_LISTADO_PDI)
       
		if success:
			#return HttpResponse(parametrosPeticion)
			try:	
				
				lista_puntos_de_interes = obtenerListadoPuntosDeInteres(parametrosPeticion["latitud"],parametrosPeticion["longitud"],parametrosPeticion["rangoMaximoAlcance"])
				return	render_to_json("PDI/respuesta/puntoDeInteres.json",{'codigo':100, 'lista_pdi':lista_puntos_de_interes})
			except Exception,err:
				   
				   return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err})
					
		else:			
			
			return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros son incorrectos'})
	else:
		
		return	render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La peticion no es post'})
		
				
