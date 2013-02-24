from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Usuario import *;
from api_puntoDeInteres import *;
from strings import *;

CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];

CODIGO_CORREO_INVALIDO=1;
CODIGO_CONTRASENIA_INVALIDA=2;
CODIGO_CORREO_REPETIDO=3;

CODIGO_INICIO_SESION_EXITOSO=0;
CODIGO_INICIO_SESION_FALLIDO=1;
CODIGO_USUARIO_NO_EXISTE=2;

def peticionRegistrarUsuario(request):
    if request.method=="POST":
        exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
        if(exito and sonParametrosValidosRegistroUsuario(parametros['correo'],parametros['contrasenia'])):
            registroExitoso=registrarUsuario(parametros["correo"],parametros["contrasenia"]);
            if(registroExitoso==CODIGO_CORREO_INVALIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CORREO_INVALIDO});
            if(registroExitoso==CODIGO_CONTRASENIA_INVALIDA):            
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CONTRASENIA_INVALIDA});
            if(registroExitoso==CODIGO_CORREO_REPETIDO):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_CORREO_REPETIDO});
            else:                                
                return render_to_json("PDI/respuesta/registroUsuario.json",{'codigo':100, 'usuario':registroExitoso}); 
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION});
       
def peticionIniciarSesion(request):
    if(request.method=="POST"):
        exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
        parametrosValidos=sonParametrosValidosRegistroUsuario(parametros['correo'],parametros['contrasenia']);
        if(parametrosValidos):
            respuesta=iniciarSesion(parametros["correo"],parametros["contrasenia"]);
            if(respuesta==CODIGO_INICIO_SESION_EXITOSO):
                listaPDI=obtenerPDIsDeUsuario(parametros["correo"]);
                return render_to_json("PDI/respuesta/inicioSesion.json",{"codigo":100,'lista_pdi':listaPDI});
            if(respuesta==CODIGO_INICIO_SESION_FALLIDO):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_ERROR_INICIO_SESION});
            if(respuesta==CODIGO_USUARIO_NO_EXISTE):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':USUARIO_MENSAJE_USUARIO_NO_EXISTE});
        else:        
            return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS});                     
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':GENERAL_MENSAJE_ERROR_TIPO_PETICION}); 
    
    
    
    
    
                  