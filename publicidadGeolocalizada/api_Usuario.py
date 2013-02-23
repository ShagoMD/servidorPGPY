from django.contrib.auth.models import User
from conversionTipos import *
from utilidades import *
import re
CODIGO_CORREO_INVALIDO=1;
CODIGO_CONTRASENIA_INVALIDA=2;
CODIGO_ERROR_CREACION_USUARIO=3;

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

def sonParametrosValidosRegistroUsuario(correo_e,password):
    if correo_e==None or not esTipoValido(correo_e,TIPO_CADENA):
        return False;
    if password==None or not esTipoValido(password,TIPO_CADENA):
        return False;    
    return True;