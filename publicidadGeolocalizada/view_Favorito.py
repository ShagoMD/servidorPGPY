
"""
view_Favorito.py: Se encarga de las funcionalidades asociadas
a marcar y desmarcar un PDI como favorito de parte de un usuario

@author Eric Huerta
@date 03/03/2013
"""

from django.shortcuts import render_to_response
from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Favorito import *;
from strings import *;

CAMPOS_FAVORITO=["idPDI","correo_e","marcado"];
CAMPOS_CONFIRMAR_FAVORITO=["usuario","idPDI"];

CODIGO_OPERACION_EXITOSA=0;

def peticionMarcarPDIcomoFavorito(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_FAVORITO)
        
        if(success):
            
            marcacionExitoso = marcarPDIcomoFavorito(params["idPDI"],params["correo_e"],params["marcado"])                
            
            if(marcacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(marcacionExitoso == CODIGO_CORREO_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(marcacionExitoso == CODIGO_MARCADO_INVAIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_CODIGO_MARCADO_INVAIDO})
            if(marcacionExitoso == CODIGO_NOTIFICACIONES_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_CODIGO_NOTIFICACION_INVALIDO})
            if(marcacionExitoso == CODIGO_DE_OPCIONES_DE_MARCADO_INCORRECTO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_CODIGO_MARCADO_INCORRECTO})
            if(marcacionExitoso == CODIGO_NO_EXISTE_PDI):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(marcacionExitoso == CODIGO_NO_EXISTE_USER):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE})
            if(marcacionExitoso == CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_PDI_YA_SE_ENCUENTRA_MARCADO})
            if(marcacionExitoso == CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_PDI_NO_SE_ENCUENTRA_MARCADO})
            if(marcacionExitoso == CODIGO_DESMARCACION_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            if(marcacionExitoso == CODIGO_MARCACION_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:
                
                if(int(float(params["marcado"])) == 0):
                    return render_to_json("PDI/respuesta/favorito.json",{'codigo':100, 'mensaje':FAVORITO_MENSAJE_MARCACION_EXITOSA, 'pdi':marcacionExitoso})
                else:
                    return render_to_json("PDI/respuesta/favorito.json",{'codigo':100, 'mensaje':FAVORITO_MENSAJE_DESMARCACION_EXITOSA, 'pdi':marcacionExitoso})
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})

def peticionEsPDIFavoritoDelUsuario(request):    
    if request.method!="POST":
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});    
    
    exito,parametros=extract_params(request.POST,CAMPOS_CONFIRMAR_FAVORITO);
    if not exito:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
    
    codigoRespuesta,respuesta=esPDIFavoritoDelUsuario(parametros["usuario"],parametros["idPDI"]);
    
    if(codigoRespuesta==FAVORITO_MENSAJE_ES_FAVORITO or codigoRespuesta==FAVORITO_MENSAJE_NO_ES_FAVORITO):
        return render_to_json("PDI/respuesta/confirmarFavorito.json",{'codigo':100,'mensaje':codigoRespuesta,'objeto':respuesta});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});
