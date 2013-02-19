from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Usuario import *;

CAMPOS_REGISTRAR_USUARIO=["correo","contrasenia"];

def peticionRegistrarUsuario(request):
    if request.method=="POST":
        exito,parametros=extract_params(request.POST,CAMPOS_REGISTRAR_USUARIO);
        if(exito and sonParametrosValidosRegistroUsuario(parametros['correo'],parametros['contrasenia'])):
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
                    