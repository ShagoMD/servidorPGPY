# -*- encoding: utf-8 -*-
#La línea de arriba es para que python reconosca el ascii de las letras con acento
"""
view_usuario.py: Se encarga de las funcionalidades asociadas
al usuario, tales como registrar el usuario asi como la de
actualizar la iformaci�n de su perfil

@author Eric Huerta
@date 10/03/2013
"""

from django.http import HttpResponse
from utilidades import *
from django.template import RequestContext
from api_Usuario import *
from django.shortcuts import render_to_response
from strings import *;

CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];
CAMPOS_ACTUALIZAR_DATOS_DEL_PERFIL = ["idUser","correo","contrasenia","nombre","apellido","URLimagen","edad","genero"]

def peticionRegistrarUsuario(request):
    if request.method=="POST":
        exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
        if(exito):
            registroExitoso=registrarUsuario(parametros["correo"],parametros["contrasenia"]);
            if(registroExitoso==1):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Introduzca un correo electronico valido.'});
            if(registroExitoso==2):            
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La contrasenia debe tener al menos 8 caracteres, una minuscula, una mayuscula y un digito.'});
            if(registroExitoso==3):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El correo introducido ya ha sido registrado en el sistema.'});
            else:                                
                return render_to_json("PDI/respuesta/registroUsuario.json",{'codigo':100, 'usuario':registroExitoso}); 
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'No se pueden procesar peticiones por GET.'});
                    
                    
                    
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
    
    
    
    
            