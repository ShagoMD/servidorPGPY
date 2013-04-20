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
from api_Favorito import *
from django.shortcuts import render_to_response
from strings import *;
from api_puntoDeInteres import *;
from strings import *;
import re

CARACTER_ESPACIO=re.compile('^\s+$');
CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];
CAMPOS_ACTUALIZAR_DATOS_DEL_PERFIL = ["correo","contrasenia","nombre","apellido","URLimagen","edad","genero"]
CAMPOS_OBTENER_PERFIL = ["correo"]

CAMPOS_LISTAR_PDIs_USUARIO=["usuario"];
 
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
            
            if(len(parametros["URLimagen"])==0 or CARACTER_ESPACIO.match(parametros["URLimagen"])):
                actualizarDatosExitoso = actualizarDatosDelPerfil(parametros["correo"],parametros["contrasenia"],parametros["nombre"],parametros["apellido"],request.build_absolute_uri('/geoAdds/media/logo/usuario.jpg'),parametros["edad"],parametros["genero"])
            else:
                actualizarDatosExitoso = actualizarDatosDelPerfil(parametros["correo"],parametros["contrasenia"],parametros["nombre"],parametros["apellido"],parametros["URLimagen"],parametros["edad"],parametros["genero"])

            if(actualizarDatosExitoso == CODIGO_USUARIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE});

            if(actualizarDatosExitoso == CODIGO_CONTRASENIA_NO_VALIDA):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CONTRASENIA_INVALIDA});
            
            if(actualizarDatosExitoso == CODIGO_ACTUALIZACION_FALLIDA):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_ACTUALIZACION_FALLIDA});
            else:
                return render_to_json("PDI/respuesta/actualizacionUsuario.json",{'codigo':100, 'mensaje':USUARIO_MENSAJE_ACTUALIZACION_EXISTOSA, 'usuario':actualizarDatosExitoso});
        else:
            return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS});
        
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    
def peticionObtenerPDIsDeUsuario(request):
    if request.method!="POST":
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});    
    
    exito,parametros=extract_params(request.POST,CAMPOS_LISTAR_PDIs_USUARIO);
    if not exito:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
    
    codigoRespuesta,listaPDI=obtenerPDIsDeUsuario(parametros["usuario"]);
    
    if(codigoRespuesta==CODIGO_REGISTRO_EXITOSO):
        return render_to_json("PDI/respuesta/inicioSesion.json",{'codigo':100,'mensaje':PDI_MENSAJE_LISTA_OBTENIDA,'lista_pdi':listaPDI});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta});

def peticionObtenerFavoritosDeUsuario(request):      
    if request.method!="POST":
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});    
    
    exito,parametros=extract_params(request.POST,CAMPOS_LISTAR_PDIs_USUARIO);
    if not exito:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});
    
    codigoRespuesta,listaFavoritos=obtenerFavoritosDeUsuario(parametros["usuario"]);
    
    if(codigoRespuesta==CODIGO_REGISTRO_EXITOSO):
        return render_to_json("PDI/respuesta/inicioSesion.json",{'codigo':100,'mensaje':PDI_MENSAJE_LISTA_FAVORITOS_OBTENIDA,'lista_pdi':listaFavoritos});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200,'mensaje':codigoRespuesta}); 
    
     
def peticionObtenerPerfilDeUsuario(request):
    
    if request.method == "POST":
        exito, parametros = extract_params(request.POST,CAMPOS_OBTENER_PERFIL)
        
        if(exito):
            
            obtenerPerfilDeUsuarioExitoso = obtenerPerfilDeUsuario(parametros["correo"])

            if(obtenerPerfilDeUsuarioExitoso == CODIGO_USUARIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE});
            else:
                return render_to_json("PDI/respuesta/actualizacionUsuario.json",{'codigo':100, 'mensaje':USUARIO_MENSAJE_OBTENER_PERFIL, 'usuario':obtenerPerfilDeUsuarioExitoso});
        else:
            return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCORRECTOS});
        
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
    
    