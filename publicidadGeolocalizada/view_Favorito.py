
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

CAMPOS_FAVORITO=["idPDI","idUser"]

def peticionMarcarPDIcomoFavorito(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_FAVORITO)
        
        if(success):
            
            marcacionExitoso = marcarPDIcomoFavorito(params["idPDI"],params["idUser"])
            
            if(marcacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(marcacionExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(marcacionExitoso == CODIGO_NO_EXISTE_PDI):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(marcacionExitoso == CODIGO_NO_EXISTE_USER):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE})
            if(marcacionExitoso == CODIGO_PDI_YA_SE_ENCUENTRA_MARCADO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_PDI_YA_SE_ENCUENTRA_MARCADO})
            if(marcacionExitoso == CODIGO_MARCACION_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'mensaje':FAVORITO_MENSAJE_MARCACION_EXITOSA}) 
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
         
         
def peticionDesmarcarPDIcomoFavorito(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_FAVORITO)
        
        if(success):
            
            desmarcacionExitoso = desmarcarPDIcomoFavorito(params["idPDI"],params["idUser"])
            
            if(desmarcacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(desmarcacionExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(desmarcacionExitoso == CODIGO_NO_EXISTE_PDI):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(desmarcacionExitoso == CODIGO_NO_EXISTE_USER):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE})
            if(desmarcacionExitoso == CODIGO_PDI_NO_SE_ENCUENTRA_MARCADO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':FAVORITO_MENSAJE_PDI_NO_SE_ENCUENTRA_MARCADO})
            if(desmarcacionExitoso == CODIGO_DESMARCACION_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'mensaje':FAVORITO_MENSAJE_DESMARCACION_EXITOSA}) 
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
         
         
