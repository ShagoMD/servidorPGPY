from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from api_Categoria import *
from models import *
from utilidades import *
from strings import *

CAMPOS_CATEGORIA=["categoria"];

CODIGO_REGISTRO_EXITOSO=0;
CODIGO_PARAMETRO_INVALIDO=-1;
CODIGO_PARAMETRO_VACIO=-2;


def peticionRegistrarCategoria(request):
    if request.method=='POST':
        exito,parametros=extract_params(request.POST,CAMPOS_CATEGORIA);
        if exito:
            respuesta=registrarCategoria(parametros); 
            if(respuesta==CODIGO_PARAMETRO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':CATEGORIA_MENSAJE_CATEGORIA_INVALIDA});
            if(respuesta==CODIGO_PARAMETRO_VACIO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':CATEGORIA_MENSAJE_CATEGORIA_VACIA});
            else:
                return render_to_json("PDI/respuesta/registroCategoria.json",{"codigo":100,"categoria":respuesta});
        else:
            return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});