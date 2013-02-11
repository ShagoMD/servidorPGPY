from models import *
import re

def registrarUsuario(correo_e,password):
    correoValido=esCorreoValido(correo_e);
    contraseniaValida=esContraseniaValida(password);
    if not correoValido:
        return 1;#el correo electrónico no cumple la forma especificada
    if not contraseniaValida:
        return 2;#la contrasenia no cumple los requisitos
    
    nuevoUsuario=Usuario(correoElectronico=correo_e,contrasenia=password);
    try:
        nuevoUsuario.save();
        return 0;#Usuario creado y registrado
    except Exception,err:
        return 3;#el correo ya existe

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
