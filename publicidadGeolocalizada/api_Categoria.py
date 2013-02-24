from models import *
from conversionTipos import *

CODIGO_REGISTRO_EXITOSO=0;
CODIGO_PARAMETRO_INVALIDO=-1;
CODIGO_PARAMETRO_VACIO=-2;


def registrarCategoria(parametros):  
    respuesta=sonParametrosValidos(parametros)
    if respuesta==True:
        nombreCat=parametros["categoria"];
        categoria=Categoria();
        categoria.nombre=nombreCat;
        categoria.save();
        return categoria;
    else:
        return respuesta;
    
def sonParametrosValidos(parametros):
    categoria=parametros["categoria"];
    if categoria=="":
        return CODIGO_PARAMETRO_VACIO;
    if categoria!="" and not esTipoValido(categoria,TIPO_CADENA):
        return CODIGO_PARAMETRO_INVALIDO;
    return True;
    