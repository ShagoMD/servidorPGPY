from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import re;

def _extract_params(request, fields, mandatory=False):
    
    fields_dict = {}

    for field in fields:
        if not field in request:
            if mandatory:
                return False, field
        else:
            fields_dict[field] = request[field]

    return True, fields_dict

def extract_params(request, mandatory_fields, optional_fields=None):
    params = {}
    params_opt = {}
    
    success, params = _extract_params (request, mandatory_fields, True)
    
    if not success:
        return False, params

    if optional_fields != None:
        success, params_opt = _extract_params (request, optional_fields, False)
        params.update(params_opt)
    
    return True, params

def render_to_json(*args, **kwargs):
    
    response = render_to_response(*args, **kwargs)
    #response['mimetype'] = "application/json"
    response['Pragma'] = "no cache"
    response['Cache-Control'] = "no-cache, must-revalidate"
    response['Content-Type'] = "application/json"

    return response

def esUsuarioValido(correo_e):
    try:
        usuario=User.objects.get(email__exact=correo_e);            
        return usuario;
    except Exception,err:
        return False;

def esURLValida(url):
    regex=re.compile('^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)( [a-zA-Z0-9\-\.\?\,\'\/\\\+&%\$#_]*)?$');
    resultado=regex.match(url);
    if resultado:
        return True;
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