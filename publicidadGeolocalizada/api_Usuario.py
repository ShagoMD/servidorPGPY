from django.contrib.auth.models import User
import re

def registrarUsuario(correo_e,password):
    correoValido=esCorreoValido(correo_e);
    contraseniaValida=esContraseniaValida(password);
    if not correoValido:
        return 1;   
    if not contraseniaValida:
        return 2;   
    
    
    try:
        nuevoUsuario=User.objects.create_user(correo_e,correo_e, password);
        nuevoUsuario.save();
        return nuevoUsuario;
    except Exception,err:
        return 3;

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
