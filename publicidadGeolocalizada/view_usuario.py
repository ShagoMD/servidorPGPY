from django.shortcuts import render_to_response;
from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Usuario import *;

CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];

def peticionRegistrarUsuario(request):
    if request.method=="POST":
        exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
        if(exito):
            registroExitoso=registrarUsuario(parametros["correo"],parametros["contrasenia"]);
            if(registroExitoso):
                return render_to_json("PDI/respuesta/error.json",{'codigo':100, 'mensaje':Usuario_Registrado});
            else:
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err});
        else:
            return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':err});    