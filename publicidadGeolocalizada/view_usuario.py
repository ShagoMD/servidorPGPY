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
            if(registroExitoso==0):
                return render_to_json("PDI/respuesta/error.json",{'codigo':100, 'mensaje':'Usuario Registrado.'});          
            if(registroExitoso==1):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Introduzca un correo electr�nico v�lido.'});
            if(registroExitoso==2):            
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'La contrase�a debe tener al menos 8 caracteres, una min�scula, una may�scula y un d�gito.'});
            if(registroExitoso==3):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El correo introducido ya ha sido registrado en el sistema.'});
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'No se pueden procesar peticiones por GET.'});
                    