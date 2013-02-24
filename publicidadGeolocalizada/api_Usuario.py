from django.contrib.auth.models import User
from conversionTipos import *
from utilidades import *
import re
CODIGO_CORREO_INVALIDO=1;
CODIGO_CONTRASENIA_INVALIDA=2;
CODIGO_ERROR_CREACION_USUARIO=3;

CODIGO_INICIO_SESION_EXITOSO=0;
CODIGO_INICIO_SESION_FALLIDO=1;
CODIGO_USUARIO_NO_EXISTE=2;

def registrarUsuario(correo_e,password):
    correoValido=esCorreoValido(correo_e);
    contraseniaValida=esContraseniaValida(password);
    if not correoValido:
        return CODIGO_CORREO_INVALIDO;   
    if not contraseniaValida:
        return CODIGO_CONTRASENIA_INVALIDA;   
    
    try:
        nuevoUsuario=User.objects.create_user(correo_e,correo_e, password);
        nuevoUsuario.save();
        return nuevoUsuario;
    except Exception,err:
        return CODIGO_ERROR_CREACION_USUARIO;

def iniciarSesion(correo_e,password):
    try:
        usuario=User.objects.get(email__exact=correo_e);            
        if(usuario.check_password(password)):
            return CODIGO_INICIO_SESION_EXITOSO;
        else:
            return CODIGO_INICIO_SESION_FALLIDO;
    except Exception,err:
        return CODIGO_USUARIO_NO_EXISTE;
    
def sonParametrosValidosRegistroUsuario(correo_e,password):
    if correo_e=="" or not esTipoValido(correo_e,TIPO_CADENA):
        return False;
    if password=="" or not esTipoValido(password,TIPO_CADENA):
        return False;    
    return True;