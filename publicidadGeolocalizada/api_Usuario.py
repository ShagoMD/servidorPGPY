from models import *

def registrarUsuario(correo_e,password):
    correoValido=esCorreoValido(correo_e);
    correoNuevo=esCorreoNuevo(correo_e);
    contraseniaValida=esContraseniaValida(contrasenia);
    if correoValido & correoNuevo & contraseniaValida:
        nuevoUsuario=Usuario(correoElectronico=correo_e,contrasenia=password);
        nuevoUsuario.save();
        return true;
    else:
        return false;

def esCorreoValido(correo_e):
    return true;

def esCorreoNuevo(correo_e):
    return rue;
    
def esContraseniaValida(contrasenia):
    return true;
