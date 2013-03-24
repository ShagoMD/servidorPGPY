# -*- encoding: utf-8 -*-
#La línea de arriba es para que python reconosca el ascii de las letras con acento
"""
view_usuario.py: Se encarga de las funcionalidades asociadas
al usuario, tales como registrar el usuario asi como la de
actualizar la iformación de su perfil

@author Eric Huerta
@date 10/03/2013
"""

from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_Usuario import *
from django.shortcuts import render_to_response
from strings import *;
from api_puntoDeInteres import *;
from strings import *;

CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];
CAMPOS_ACTUALIZAR_DATOS_DEL_PERFIL = ["idUser","correo","contrasenia","nombre","apellido","URLimagen","edad","genero"]

CODIGO_CORREO_INVALIDO=1;
CODIGO_CONTRASENIA_INVALIDA=2;
CODIGO_CORREO_REPETIDO=3;

CODIGO_INICIO_SESION_EXITOSO=0;
CODIGO_INICIO_SESION_FALLIDO=1;
CODIGO_USUARIO_NO_EXISTE=2;
CODIGO_OPERACION_EXITOSA=0;

def peticionRegistrarUsuario(request):
    if request.method!="POST":        
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
    
    if not exito:        
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});                     
    
    codigoRespuesta,usuario=registrarUsuario(parametros["correo"],parametros["contrasenia"]);

    if(codigoRespuesta==CODIGO_OPERACION_EXITOSA):            
        return render_to_json("PDI/respuesta/registroUsuario.json",{'codigo':100,'mensaje':USUARIO_MENSAJE_REGISTRO_EXITOSO,'usuario':usuario});       
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':codigoRespuesta});                               

       
def peticionIniciarSesion(request):
    if(request.method!="POST"):        
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION}); 

    exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
    if not exito:            
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});                     
       
    codigoRespuesta,listaPDI=iniciarSesion(parametros["correo"],parametros["contrasenia"]);

    if(codigoRespuesta==CODIGO_OPERACION_EXITOSA):
        return render_to_json("PDI/respuesta/inicioSesion.json",{"codigo":100,'mensaje':USUARIO_MENSAJE_INICIO_SESION_EXITOSO,'lista_pdi':listaPDI});
    else:                
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':codigoRespuesta});     
                    
def peticionActualizarDatosDelPerfil(request):
    
    if request.method == "POST":
        exito, parametros = extract_params(request.POST,CAMPOS_ACTUALIZAR_DATOS_DEL_PERFIL)
        
        if(exito):
            actualizarDatosExitoso = actualizarDatosDelPerfil(parametros["idUser"],parametros["correo"],parametros["contrasenia"],parametros["nombre"],parametros["apellido"],parametros["URLimagen"],parametros["edad"],parametros["genero"])
            
            if(actualizarDatosExitoso == CODIGO_ID_USER_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_ID_DEL_USUARIO_INVALIDO});
            
            if(actualizarDatosExitoso == CODIGO_ACTUALIZACION_VACIA):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_ACTUALIZACION_VACIA});
            
            if(actualizarDatosExitoso == CODIGO_DUPLICIDAD_DE_CORREOS):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CORREO_REPETIDO});
            
            if(actualizarDatosExitoso == CODIGO_USUARIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE});
            
            if(actualizarDatosExitoso == CODIGO_CORREO_NO_VALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CORREO_INVALIDO});
            
            if(actualizarDatosExitoso == CODIGO_CONTRASENIA_NO_VALIDA):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CONTRASENIA_INVALIDA});
            
            if(actualizarDatosExitoso == CODIGO_ACTUALIZACION_EXITOSA):
                return render_to_json("PDI/respuesta/error.json",{'codigo':100, 'mensaje':USUARIO_MENSAJE_ACTUALIZACION_EXISTOSA}); 
            else:
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_ACTUALIZACION_FALLIDA});
            
        else:
            return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS});
        
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    
    
    
            