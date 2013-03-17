from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from api_Categoria import *
from models import *
from utilidades import *
from strings import *

CAMPOS_CATEGORIA=["categoria"];
CAMPOS_ELIMINAR_CATEGORIA=["idCategoria","nombreCategoria"];

def peticionRegistrarCategoria(request):
    if request.method=='POST':
        exito,parametros=extract_params(request.POST,CAMPOS_CATEGORIA);
        
        if not exito:            
            return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
        
        codigoRespuesta,categoria=registrarCategoria(parametros); 
        
        if(codigoRespuesta==CODIGO_OPERACION_EXITOSA):                    
            return render_to_json("PDI/respuesta/categoria.json",{'codigo':100,'mensaje':CATEGORIA_MENSAJE_REGISTRO_EXITOSO,'id':categoria.id});
        else:                
            return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});
        
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
def peticionEliminarCategoria(request):
    if request.method!='POST':        
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    exito,parametros=extract_params(request.POST,CAMPOS_ELIMINAR_CATEGORIA);
    
    if not exito:            
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
                
    codigoRespuesta,categoria=eliminarCategoria(parametros);         
    
    if(codigoRespuesta==CODIGO_OPERACION_EXITOSA):                    
        return render_to_json("PDI/respuesta/categoria.json",{'codigo':100,'mensaje':CATEGORIA_MENSAJE_CATEGORIA_ELIMINADA,'id':categoria});
    else:                
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});


        
def peticionActualizarCategoria(request):    
    if request.method!='POST':        
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    exito,parametros=extract_params(request.POST,CAMPOS_ELIMINAR_CATEGORIA);
    
    if not exito:            
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
                
    codigoRespuesta,categoria=actualizarCategoria(parametros);         
    
    if(codigoRespuesta==CODIGO_OPERACION_EXITOSA):                    
        return render_to_json("PDI/respuesta/categoria.json",{'codigo':100,'mensaje':CATEGORIA_MENSAJE_ACTUALIZADA,'id':categoria.id});
    else:                
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});