from models import *
import re

def registrarUsuario(correo_e,password):
    correoValido=esCorreoValido(correo_e);
    correoNuevo=True;#esCorreoNuevo(correo_e);
    contraseniaValida=esContraseniaValida(password);
    if correoValido & correoNuevo & contraseniaValida:
        nuevoUsuario=Usuario(correoElectronico=correo_e,contrasenia=password);
        try:
            nuevoUsuario.save();
            return True;
        except Exception,err:
            return False;
    else:
        return False;

def esCorreoValido(correo_e):
    regex=re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$');
    resultado=regex.match(correo_e);
    if resultado:
            return True;
    else:
        return False;
    
def esContraseniaValida(contrasenia):
    regex=re.compile('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$');
    resultado=regex.match(contrasenia);
    if resultado:
        return True;
    else:
        return False;
