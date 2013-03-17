from django.shortcuts import render_to_response
from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_puntoDeInteres import *
from strings import *

CAMPOS_OBLIGATORIOS_REGISTRO_PDI = ["usuario","latitud","longitud","altitud","nombre","categoria"];
CAMPOS_OPCIONALES_REGISTRO_PDI = ["descripcion","direccion","paginaWeb","telefono","email","imagen"];

CAMPOS_OBLIGATORIOS_ACTUALIZAR_PDI=["usuario","idPDI"];
CAMPOS_OPCIONALES_ACTUALIZAR_PDI=["descripcion","direccion","paginaWeb","telefono","email"];

CAMPOS_LISTADO_PDI = ["latitud","longitud","rangoMaximoAlcance"];

CAMPOS_ELIMINAR_PDI=["usuario","idPDI"];
CAMPOS_ELIMINAR_TODOS_PDI=["usuario"];

CODIGO_REGISTRO_EXITOSO=0;
CODIGO_LOCALIZACION_REPETIDA=1;
CODIGO_LIMITE_PDI_ALCANZADO=2;
CODIGO_USUARIO_INVALIDO=3;
CODIGO_CATEGORIA_INVALIDA=4;
CODIGO_PDI_NO_EXISTE=5;
CODIGO_PDI_ELIMINADO=6;
CODIGO_NO_HAY_PDIs_REGISTRADOS=7;

def peticionRegistrarPDI(request):
	if request.method != "POST":		
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});		
	
	exito, parametrosObligatorios = extract_params(request.POST,CAMPOS_OBLIGATORIOS_REGISTRO_PDI);
	if not exito:			
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});						

	codigoRespuesta,pdi=registrarPuntoDeInteres(parametrosObligatorios);		
	
	if(codigoRespuesta==CODIGO_REGISTRO_EXITOSO):					
		return render_to_json("PDI/respuesta/pdi.json",{'codigo':100,'mensaje':PDI_MENSAJE_REGISTRO_EXITOSO,'pdi':pdi});
	else:				
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});		
	
def peticionActualizarPDI(request):
	if request.method!="POST":	
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});	
	
	exito, parametrosObligatorios = extract_params(request.POST,CAMPOS_OBLIGATORIOS_ACTUALIZAR_PDI);
	exito2,parametrosOpcionales=extract_params(request.POST,CAMPOS_OPCIONALES_ACTUALIZAR_PDI);		
	
	if not exito:			
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});	
	
	codigoRespuesta,pdi=actualizarPuntoDeInteres(parametrosObligatorios,parametrosOpcionales);

	if(codigoRespuesta==CODIGO_REGISTRO_EXITOSO):					
		return render_to_json("PDI/respuesta/pdi.json",{'codigo':100,'mensaje':PDI_MENSAJE_PDI_ACTUALIZADO,'pdi':pdi});
	else:				
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});		


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
	
def peticionEliminarPDI(request):
	if request.method!="POST":
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});	
	
	exito,parametros=extract_params(request.POST,CAMPOS_ELIMINAR_PDI);
	if not exito:
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
	
	codigoRespuesta,pdi=eliminarPuntoDeInteres(parametros["usuario"],parametros["idPDI"]);
	
	if(codigoRespuesta==CODIGO_REGISTRO_EXITOSO):
		return render_to_json("PDI/respuesta/pdi.json",{'codigo':100,'mensaje':PDI_MENSAJE_PDI_ELIMINADO,'pdi':pdi});
	else:
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});
	
				
def peticionEliminarTodosPDI(request):
	if request.method=="POST":	
		exito,parametros=extract_params(request.POST,CAMPOS_ELIMINAR_TODOS_PDI);
		if(exito):
			respuesta=eliminarTodosPuntosDeInteresDeUsuario(parametros["usuario"]);
			if (respuesta==CODIGO_USUARIO_INVALIDO):
				return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':PDI_MENSAJE_USUARIO_INVALIDO});
			if(respuesta==CODIGO_NO_HAY_PDIs_REGISTRADOS):
				return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':PDI_MENSAJE_NO_HAY_PDIs_REGISTRADOS});
			if(respuesta==CODIGO_PDI_ELIMINADO):				
				return render_to_json("PDI/respuesta/eliminarPDI.json",{'codigo':100,'mensaje':PDI_MENSAJE_TODOS_PDIS_ELIMINADOS});
		else:
			return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});		
	else:
		return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	