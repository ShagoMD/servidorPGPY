from models import *
from conversionTipos import *
from strings import *


CODIGO_OPERACION_EXITOSA=0;

def registrarCategoria(parametros):  
    respuesta=sonParametrosValidosRegistrar(parametros);    
    categoria=Categoria();
    
    if respuesta is not True:
        return respuesta,categoria;
        
    nombreCat=parametros["categoria"];
    if existeCategoria(nombreCat):
        return CATEGORIA_MENSAJE_CATEGORIA_DUPLICADA,categoria;
    

    categoria.nombre=nombreCat;
    categoria.save();
    
    return CODIGO_OPERACION_EXITOSA,categoria;

def actualizarCategoria(parametros):
    respuesta=sonParametrosValidosActualizar(parametros);    
    categoria=Categoria();
    
    if respuesta is not True:
        return respuesta,categoria;
    
    nombreCat=parametros["nombreCategoria"];
    idCat=parametros["idCategoria"]
     
    try:
        categoria=Categoria.objects.get(pk=idCat);
    except Exception,err:
        return CATEGORIA_MENSAJE_CATEGORIA_NO_EXISTE,categoria;
    
    if existeCategoria(nombreCat) is True:
        return CATEGORIA_MENSAJE_NOMBRE_EXISTE,categoria;
    
    categoria.nombre=nombreCat;
    categoria.save();    
    
    return CODIGO_OPERACION_EXITOSA,categoria;

        
def eliminarCategoria(parametros):
    validacion=sonParametrosValidosEliminar(parametros);
    categoria=Categoria();
    
    if validacion is not True:
        return validacion,categoria;
    idCat=parametros["idCategoria"];
    nombreCat=parametros["nombreCategoria"];
    
    if idCat!="":
        try:
            categoria=Categoria.objects.get(pk=idCat);
        except Exception,err:
            return CATEGORIA_MENSAJE_CATEGORIA_NO_EXISTE,categoria;
    else:
        categoria=Categoria.objects.filter(nombre__exact=nombreCat);
        if(len(categoria)>0):
            categoria=categoria[0];
        else:            
            return CATEGORIA_MENSAJE_CATEGORIA_NO_EXISTE,categoria;
    try:
        id=categoria.id;
        categoria.delete();
        return CODIGO_OPERACION_EXITOSA,id;
    except Exception,err:
        return CATEGORIA_MENSAJE_ERROR_ELIMINAR,categoria;
    
    
def sonParametrosValidosRegistrar(parametros):
    categoria=parametros["categoria"];
    if categoria=="":
        return CATEGORIA_MENSAJE_CATEGORIA_VACIA;
    if categoria!="" and not esTipoValido(categoria,TIPO_CADENA):
        return CATEGORIA_MENSAJE_CATEGORIA_INVALIDA;
    
    return True;

def sonParametrosValidosEliminar(parametros):
    idCat=parametros["idCategoria"];
    nombreCat=parametros["nombreCategoria"];
    
    if(idCat=="" and nombreCat==""):
        return CATEGORIA_MENSAJE_PARAMETROS_VACIOS;
    if (idCat!="" and not esTipoValido(idCat,TIPO_ENTERO)):
        return CATEGORIA_MENSAJE_ID_INVALIDO;

    if(idCat=="" and nombreCat!="" and not esTipoValido(nombreCat,TIPO_CADENA)):
        return CATEGORIA_MENSAJE_NOMBRE_INVALIDO;
    
    return True;

def sonParametrosValidosActualizar(parametros):
    idCat=parametros["idCategoria"];
    nombreCat=parametros["nombreCategoria"];
    if(idCat=="" or nombreCat==""):
        return CATEGORIA_MENSAJE_PARAMETROS_VACIOS;
    
    if (idCat!="" and not esTipoValido(idCat,TIPO_ENTERO)):
        return CATEGORIA_MENSAJE_ID_INVALIDO;
    return True;
    
def existeCategoria(nombreCat):
    listaCat=Categoria.objects.filter(nombre__exact=nombreCat);
    if(len(listaCat)==0):
        return False;
    else:
        return True;
    