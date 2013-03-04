
"""
view_Anuncio.py: Se encarga de las funcionalidades asociadas
a anuncio, tales como registrar, modificar y eliminar uno
o todos los anuncios asociados a un PDI

@author Eric Huerta
@date 02/03/2013
"""

from django.shortcuts import render_to_response
from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Anuncio import *;
from strings import *;


CAMPOS_REGISTRAR_ANUNCIO=["idPDI","idUser","titulo","descripcion","categoria","URLimagen"]
CAMPOS_MODIFICAR_ANUNCIO=["idAnuncio","idPDI","idUser","titulo","descripcion","categoria","URLimagen"]
CAMPOS_ELIMINAR_ANUNCIO=["idAnuncio","idPDI","idUser"]
CAMPOS_ELIMINAR_TODOS_LOS_ANUNCIOS=["idPDI","idUser"]

def peticionRegistrarAnuncio(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_REGISTRAR_ANUNCIO)
        
        if(success):
            
            registroExitoso = registrarAnuncio(params["idPDI"],params["idUser"],params["titulo"],params["descripcion"],params["categoria"],params["URLimagen"])
            
            if(registroExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(registroExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(registroExitoso == CODIGO_TITULO_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_TITULO_INVALIDO})
            if(registroExitoso == CODIGO_DESCRIPCION_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_DESCRIPCION_USER_INVALIDO})
            if(registroExitoso == CODIGO_CATEGORIA_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_CATEGORIA_INVALIDO})
            if(registroExitoso == CODIGO_URL_IMAGEN_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_URL_IMAGEN_INVALIDO})
            if(registroExitoso == CODIGO_PDI_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(registroExitoso == CODIGO_PDI_NO_ES_DEL_USUARIO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PID_NO_ES_DEL_USER})
            if(registroExitoso == CODIGO_LIMITE_ANUNCIOS_ALCANZADO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_LIMITE_ANUNCIO_ALCANZADO})
            if(registroExitoso == CODIGO_REGISTRO_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'anuncio':registroExitoso}) 
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
         
         
def peticionModificarAnuncio(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_MODIFICAR_ANUNCIO)
        
        if(success):
            
            modificacionExitoso = modificarAnuncio(params["idAnuncio"],params["idPDI"],params["idUser"],params["titulo"],params["descripcion"],params["categoria"],params["URLimagen"])
            
            if(modificacionExitoso == CODIGO_ID_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_ANUNCIO_INVALIDO})
            if(modificacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(modificacionExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(modificacionExitoso == CODIGO_TITULO_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_TITULO_INVALIDO})
            if(modificacionExitoso == CODIGO_DESCRIPCION_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_DESCRIPCION_USER_INVALIDO})
            if(modificacionExitoso == CODIGO_CATEGORIA_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_CATEGORIA_INVALIDO})
            if(modificacionExitoso == CODIGO_URL_IMAGEN_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_URL_IMAGEN_INVALIDO})
            if(modificacionExitoso == CODIGO_ANUNCIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ANUNCIO_NO_EXISTE})
            if(modificacionExitoso == CODIGO_PDI_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(modificacionExitoso == CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_NO_HAY_ANUNCIOS_REGISTRADOS})
            if(modificacionExitoso == CODIGO_PDI_NO_ES_DEL_USUARIO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PID_NO_ES_DEL_USER})
            if(modificacionExitoso == CODIGO_ANUNCIO_NO_ES_DEL_PDI):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ANUNCIO_NO_ES_DEL_PDI})
            if(modificacionExitoso == CODIGO_MODIFICA_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'anuncio':modificacionExitoso}) 
            
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
        
                
def peticionEliminarAnuncio(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_ELIMINAR_ANUNCIO)
        
        if(success):
            
            eliminacionExitoso = eliminarAnuncio(params["idAnuncio"],params["idPDI"],params["idUser"])
            
            if(eliminacionExitoso == CODIGO_ID_ANUNCIO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_ANUNCIO_INVALIDO})
            if(eliminacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(eliminacionExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(eliminacionExitoso == CODIGO_ANUNCIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ANUNCIO_NO_EXISTE})
            if(eliminacionExitoso == CODIGO_PDI_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(eliminacionExitoso == CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_NO_HAY_ANUNCIOS_REGISTRADOS})
            if(eliminacionExitoso == CODIGO_PDI_NO_ES_DEL_USUARIO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PID_NO_ES_DEL_USER})
            if(eliminacionExitoso == CODIGO_ANUNCIO_NO_ES_DEL_PDI):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ANUNCIO_NO_ES_DEL_PDI})
            if(eliminacionExitoso == CODIGO_ELIMINA_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'anuncio':eliminacionExitoso}) 
            
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
    

def peticionEliminarTodoLosAnuncios(request):
    if request.method=="POST":
        
        success, params = extract_params(request.POST,CAMPOS_ELIMINAR_TODOS_LOS_ANUNCIOS)
        
        if(success):
            
            eliminacionExitoso = eliminarTodosLosAnuncios(params["idPDI"],params["idUser"])
            
            if(eliminacionExitoso == CODIGO_ID_PDI_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_PDI_INVALIDO})
            if(eliminacionExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_ID_USER_INVALIDO})
            if(eliminacionExitoso == CODIGO_PDI_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PDI_NO_EXISTE})
            if(eliminacionExitoso == CODIGO_NO_HAY_ANUNCIOS_REGISTRADOS):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_NO_HAY_ANUNCIOS_REGISTRADOS})
            if(eliminacionExitoso == CODIGO_PDI_NO_ES_DEL_USUARIO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_PID_NO_ES_DEL_USER})
            if(eliminacionExitoso == CODIGO_ELIMINA_FALLIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':ANUNCIO_MENSAJE_REGISTRO_FALLIDO})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'mensaje':ANUNCIO_MENSAJE_TODOS_LOS_ANUNCIOS_ELIMINADOS}) 
            
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION})
    
    
        