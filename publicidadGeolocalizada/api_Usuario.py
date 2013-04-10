# -*- encoding: utf-8 -*-
#La línea de arriba es para que python reconosca el ascii de las letras con acento
"""
api_Usuario.py: Se encarga de las funcionalidades asociadas
al usuario, tales como registrar el usuario asi como la de
actualizar la iformaci�n de su perfil

@author Eric Huerta
@date 10/03/2013
"""

from models import *
from django.contrib.auth.models import User
from conversionTipos import *
from utilidades import *
from django.db import connection
connection._rollback()
import re
from strings import *;
from api_puntoDeInteres import *;


CARACTER_ESPACIO=re.compile('^\s+$');
CODIGO_CORREO_INVALIDO=1;
CODIGO_CONTRASENIA_INVALIDA=2;
CODIGO_ERROR_CREACION_USUARIO=3;

CODIGO_INICIO_SESION_EXITOSO=0;
CODIGO_INICIO_SESION_FALLIDO=1;
CODIGO_USUARIO_NO_EXISTE=2;

TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'

CADENA_VACIA = 0

CODIGO_ACTUALIZACION_EXITOSA = 0
CODIGO_ACTUALIZACION_FALLIDA = 1

CODIGO_ACTUALIZACION_VACIA = 2
CODIGO_TODOS_LOS_PARAMETROS_NO_ESTAN_VACIOS = 3
CODIGO_PARAMETROS_OBLIGATORIOS_NO_ESTAN_VACIOS = 4

CODIGO_ID_USER_INVALIDO = 5
CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS = 6

CODIGO_CORREO_VACIO = 7
CODIGO_CONTRASENIA_VACIA = 8
CODIGO_NOMBRE_VACIOS = 9
CODIGO_APELLIDO_VACIOS = 10
CODIGO_URL_IMAGEN_VACIOS = 11
CODIGO_EDAD_VACIO = 12
CODIGO_GENERO_VACIO = 13

CODIGO_PARAMETRO_NO_VACIO = 14
CODIGO_DUPLICIDAD_DE_CORREOS = 15
CODIGO_NO_DUPLICIDAD_DE_CORREOS = 16

CODIGO_CORREO_NO_VALIDO = 17
CODIGO_CONTRASENIA_NO_VALIDA = 18
CODIGO_USUARIO_NO_EXISTE = 19

CODIGO_YA_TIENE_PERFIL = 20
CODIGO_PERFIL_CREADO = 21

CODIGO_OPERACION_EXITOSA=0;

def registrarUsuario(correo_e,password):
    parametrosValidos=sonParametrosValidosRegistroUsuario(correo_e,password);
    
    if parametrosValidos is not True:
        return GENERAL_MENSAJE_PARAMETROS_INCORRECTOS,False;
    
    correoValido=esCorreoValido(correo_e);
    contraseniaValida=esContraseniaValida(password);
    
    if correoValido is not True:
        return USUARIO_MENSAJE_CORREO_INVALIDO,False;   
    if contraseniaValida is not True:
        return USUARIO_MENSAJE_CONTRASENIA_INVALIDA,False;   
    
    try:
        nuevoUsuario=User.objects.create_user(correo_e,correo_e, password);
        nuevoUsuario.save();
        return CODIGO_OPERACION_EXITOSA,nuevoUsuario;
    except Exception,err:
        return USUARIO_MENSAJE_CORREO_REPETIDO,False;


#Actualizac�n de datos del perfil de Usuario
def actualizarDatosDelPerfil(idUser,correo_e,contrasenia,nombre,apellido,URLimagen,edad,genero):
    
    parametrosObligatorios = sonParametrosObligatorios(idUser)
    
    if(parametrosObligatorios == CODIGO_ID_USER_INVALIDO):
        return CODIGO_ID_USER_INVALIDO
    
    parametrosVacios = sonTodosLosParametrosVacios(correo_e,contrasenia,nombre,apellido,URLimagen,edad,genero)
    
    #Verifico que si se envian puros parametros vacios, representa una actualizacion vacia, sin cambios
    if (parametrosVacios == CODIGO_ACTUALIZACION_VACIA):
        return CODIGO_ACTUALIZACION_VACIA
    
    try:
        #Despu�s de validar que el ID del usuario no este vac�o y que sea del tipo correcto, obtengo al usuario
        usuario = User.objects.get(id=idUser)
    except User.DoesNotExist:
        return CODIGO_USUARIO_NO_EXISTE
    
    
    #Obtengo el perfil del usuario, si es que no tiene pues lo creo
    try:
        perfil = PerfilDeUsuario.objects.get(user_id=usuario.id)
    
    except Exception,err:
        perfil = PerfilDeUsuario.objects.create(user=usuario)


    #Se validad primero que el correo contenga algo para poder actualizar
    if (esCorreoVacio(correo_e) == CODIGO_PARAMETRO_NO_VACIO):
        if(existeDuplicidadDeCorreo(correo_e, idUser) == CODIGO_DUPLICIDAD_DE_CORREOS):
            return CODIGO_DUPLICIDAD_DE_CORREOS
        if not (esCorreoValido(correo_e)):
            return CODIGO_CORREO_NO_VALIDO
        #Despu�s de validar a duplicidad y que sea valido, actualizo el correo
        usuario.email = correo_e
        #Por motivos propios del registro de usuario, se maneja el correo como nombre de usuario
        usuario.username = correo_e
        
        
    #Se valida primero que la contrase�a contenga algo para poder actualizar
    if (esContraseniaVacia(contrasenia) == CODIGO_PARAMETRO_NO_VACIO):
        if not (esContraseniaValida(contrasenia)):
            return CODIGO_CONTRASENIA_NO_VALIDA
        #Despu�s de validar la contrase�a, actualizo la mencionada contrase�a
        usuario.password = contrasenia
    
    #Se valida que no este vac�o el nombre para poder actualizar
    if (esNombreVacio(nombre) == CODIGO_PARAMETRO_NO_VACIO):
        usuario.first_name = nombre
        
    #Se valida que no este vac�o el apellido para poder actualizar
    if (esApellidoVacio(apellido) == CODIGO_PARAMETRO_NO_VACIO):
        usuario.last_name = apellido
    
    #Se valida que no este vac�o la URL de la imagen para poder actualizar
    if (esURLimagenVacio(URLimagen) == CODIGO_PARAMETRO_NO_VACIO):
        perfil.rutaImagen = URLimagen
        #usuario.get_profile().rutaImagen = URLimagen
    
    #Se valida que no este vac�a la edad para poder actualizar
    if (esEdadVacia(edad) == CODIGO_PARAMETRO_NO_VACIO):
        perfil.edad = edad
        #usuario.get_profile().edad = edad
    
    #Se valida que no este vac�o el genero para poder actualizar
    if (esGeneroVacio(genero) == CODIGO_PARAMETRO_NO_VACIO):
        perfil.genero = genero
        #usuario.get_profile().genero = genero
    
    try:
        #Actualizo el perfil del usuario, así como el usuario en sí
        usuario.save()
        perfil.save()
        #usuario.get_profile().save
        return CODIGO_ACTUALIZACION_EXITOSA
    except Exception,err:
        return CODIGO_ACTUALIZACION_FALLIDA
    

    

def iniciarSesion(correo_e,password):
    parametrosValidos=sonParametrosValidosRegistroUsuario(correo_e, password);
    if parametrosValidos is not True:
        return GENERAL_MENSAJE_PARAMETROS_INCORRECTOS,False;
    try:
        usuario=User.objects.get(email__exact=correo_e);            
        if(usuario.check_password(password)):
            respuesta,listaPDI=obtenerPDIsDeUsuario(correo_e);
            if(respuesta==CODIGO_OPERACION_EXITOSA):
                return CODIGO_OPERACION_EXITOSA,listaPDI;
            else:
                return USUARIO_MENSAJE_USUARIO_NO_EXISTE,False;
        else:
            return USUARIO_MENSAJE_ERROR_INICIO_SESION,False;
    except Exception,err:
        return USUARIO_MENSAJE_USUARIO_NO_EXISTE,False;
    
    
def sonParametrosValidosRegistroUsuario(correo_e,password):
    if correo_e=="" or not esTipoValido(correo_e,TIPO_CADENA):
        return False;
    if password=="" or not esTipoValido(password,TIPO_CADENA):
        return False;    
    return True;
def sonTodosLosParametrosVacios(correo_e,contrasenia,nombre,apellido,URLimagen,edad,genero):
    
    if len(correo_e)==0 and len(contrasenia)==0 and len(nombre)==0 and len(apellido)==0 and len(URLimagen)==0 and len(edad)==0 and len(genero)==0 :
        return CODIGO_ACTUALIZACION_VACIA
            
    return CODIGO_TODOS_LOS_PARAMETROS_NO_ESTAN_VACIOS


def sonParametrosObligatorios(idUser):
    
    if len(idUser)==0 or not esTipoValido(idUser,TIPO_ENTERO):
        return CODIGO_ID_USER_INVALIDO
    
    return CODIGO_PARAMETROS_OBLIGATORIOS_VALIDOS


def esCorreoVacio(correo_e):
    if len(correo_e) == CADENA_VACIA:
        return CODIGO_CORREO_VACIO
    return CODIGO_PARAMETRO_NO_VACIO

def esContraseniaVacia(contrasenia):
    if len(contrasenia) == CADENA_VACIA:
        return CODIGO_CONTRASENIA_VACIA
    return CODIGO_PARAMETRO_NO_VACIO

def esNombreVacio(nombre):
    if len(nombre) == CADENA_VACIA:
        return CODIGO_NOMBRE_VACIOS
    return CODIGO_PARAMETRO_NO_VACIO

def esApellidoVacio(apellido):
    if len(apellido) == CADENA_VACIA:
        return CODIGO_APELLIDO_VACIOS
    return CODIGO_PARAMETRO_NO_VACIO

def esURLimagenVacio(URLimagen):
    if len(URLimagen) == CADENA_VACIA:
        return CODIGO_URL_IMAGEN_VACIOS
    return CODIGO_PARAMETRO_NO_VACIO

def esEdadVacia(edad):
    if len(edad) == CADENA_VACIA:
        return CODIGO_EDAD_VACIO
    return CODIGO_PARAMETRO_NO_VACIO

def esGeneroVacio(genero):
    if len(genero) == CADENA_VACIA:
        return CODIGO_GENERO_VACIO
    return CODIGO_PARAMETRO_NO_VACIO

def existeDuplicidadDeCorreo(correo_e, idUser):
    
    listaDeUsuarios = User.objects.all()
    
    if(len(listaDeUsuarios)!=CADENA_VACIA):
        for user in listaDeUsuarios:
            if(user.email == correo_e):
                if(user.id != int(float(idUser))):
                    return CODIGO_DUPLICIDAD_DE_CORREOS
    
    return CODIGO_NO_DUPLICIDAD_DE_CORREOS
