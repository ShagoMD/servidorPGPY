# -*- encoding: utf-8 -*-
#La línea de arriba es para que python reconosca el ascii de las letras con acento

#En esta seccion se colocan Strings generales que pueden ser usados por cualquier View y/o api
GENERAL_MENSAJE_ERROR_TIPO_PETICION='La peticion no fue realizada a traves de POST.';
GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO="El campo de texto es invalido.";
GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS='No se enviaron todos los parametros obligatorios.';
GENERAL_MENSAJE_PARAMETROS_INCORRECTOS='Los parametros son incorrectos.'


#En esta seccion se definen los strings usados por el View, la api y cualquier otra clase referente a PDI
PDI_MENSAJE_REGISTRO_EXITOSO='Registro de PDI exitoso';
PDI_MENSAJE_LOCALIZACION_REPETIDA='Los datos de localizacion del PDI que se desea registrar ya han sido utilizados previamente.';
PDI_MENSAJE_LIMITE_PDI_ALCANZADO='Se ha alcanzado el limite de PDI que su cuenta le permite registrar.';
PDI_MENSAJE_USUARIO_INVALIDO='El usuario no existe.';
PDI_MENSAJE_CATEGORIA_INVALIDA='La categoria sobre la cual se intenta registrar el PDI no existe.';

PDI_MENSAJE_URL_WEB_INVALIDA="La url del sitio web no tiene el formato correcto.";
PDI_MENSAJE_URL_IMAGEN_INVALIDA="La url de la imagen no tiene el formato correcto.";
PDI_MENSAJE_CORREO_INVALIDO="El correo electronico del sitio no es valido.";

PDI_MENSAJE_PDI_NO_EXISTE="El punto de interes que esta tratando de eliminar no existe.";
PDI_MENSAJE_NO_HAY_PDIs_REGISTRADOS="El usuario no tiene puntos de interes registrados.";
PDI_MENSAJE_PDI_ELIMINADO="El punto de interes y todos sus anuncion asociados fueron eliminados correctamente.";
PDI_MENSAJE_TODOS_PDIS_ELIMINADOS="Todos los puntos de interes del usuario y sus respectivos anuncios han sido eliminados correctamente.";

PDI_MENSAJE_PDI_ACTUALIZADO="Los datos del punto de interes fueron actualizados correctamente.";

#En esta seccion se definen los strings usados por el View, la api y otras clases correspondientes a Usuario
USUARIO_MENSAJE_CORREO_INVALIDO='Introduzca un correo electronico valido.';
USUARIO_MENSAJE_CONTRASENIA_INVALIDA='La contrasenia debe tener al menos 8 caracteres, una minuscula, una mayuscula y un digito.';
USUARIO_MENSAJE_CORREO_REPETIDO='El correo electronico introducido ya ha sido registrado en el sistema.';
USUARIO_MENSAJE_ERROR_INICIO_SESION='La combinacion de usuario y contrasenia utilizada no es valida.';
USUARIO_MENSAJE_USUARIO_NO_EXISTE='El usuario con el que trata de ingresar no existe.';
USUARIO_MENSAJE_ACTUALIZACION_VACIA='La actualizacion de los datos del perfil no sufrieron cambio alguno.'
USUARIO_MENSAJE_ID_DEL_USUARIO_INVALIDO='El ID del usuario es invalido.'
USUARIO_MENSAJE_ACTUALIZACION_EXISTOSA='Actualizacion de los datos del perfil exitoso.'
USUARIO_MENSAJE_ACTUALIZACION_FALLIDA='Actualizacion de los datos del perfil fallido.'

#En esta seccion se definen los strings usados por el View, la api y otras clases concernientes a Categoria
CATEGORIA_MENSAJE_CATEGORIA_INVALIDA="El valor que trata de registrar no es unca cadena de texto.";
CATEGORIA_MENSAJE_CATEGORIA_VACIA="El nombre de la Categoria se encuentra vacio.";

#En esta seccion se definen los strings usados por el View, la api, y otras clases relativas a Anuncio
ANUNCIO_MENSAJE_REGISTRO_EXITOSO='Registro del Anuncio exitoso.'
ANUNCIO_MENSAJE_REGISTRO_FALLIDO='Registro del Anuncio fallido.'

ANUNCIO_MENSAJE_ID_ANUNCIO_INVALIDO='Introdusca un id de Anuncio valido.'
ANUNCIO_MENSAJE_ID_PDI_INVALIDO='Introdusca un id de PDI valido.'
ANUNCIO_MENSAJE_ID_USER_INVALIDO='Introdusca un id de Usuario valido.'
ANUNCIO_MENSAJE_TITULO_INVALIDO='Introdusca un titulo de Anuncio valido.'
ANUNCIO_MENSAJE_DESCRIPCION_USER_INVALIDO='Introdusca una descripcion de Anuncio valida.'
ANUNCIO_MENSAJE_CATEGORIA_INVALIDO='Introdusca una categoria de Anuncio valida.'
ANUNCIO_MENSAJE_URL_IMAGEN_INVALIDO='Introdusca una URL de imagen del Anuncio valida.'

ANUNCIO_MENSAJE_ANUNCIO_NO_ES_DEL_PDI='El Anuncio no le pertenece al PDI.'
ANUNCIO_MENSAJE_PID_NO_ES_DEL_USER='El PDI no le pertenece al Usuario.'

ANUNCIO_MENSAJE_ANUNCIO_NO_EXISTE='El anuncio que indico no existe.'
ANUNCIO_MENSAJE_PDI_NO_EXISTE='El PDI que indico no existe.'
ANUNCIO_MENSAJE_NO_HAY_ANUNCIOS_REGISTRADOS='El PDI no tiene Anuncios registrados.'
ANUNCIO_MENSAJE_ANUNCIO_ELIMINADO='El anuncio del PDI fue eliminado.'
ANUNCIO_MENSAJE_TODOS_LOS_ANUNCIOS_ELIMINADOS='Todos los anuncios del PDI fueron eliminados.'

ANUNCIO_MENSAJE_ANUNCIO_ACTUALIZADO='Los datos del Anuncio de fueron actualizadas correctamente.'
ANUNCIO_MENSAJE_LIMITE_ANUNCIO_ALCANZADO='Se ha alcanzado el limite de Anuncios que su PDI le permite registrar.'

#En esta seccion se definen los strings usados por el View, la api, y otras clases relativas a Anuncio
FAVORITO_MENSAJE_MARCACION_EXITOSA='Marcacion como favorito exitoso'
FAVORITO_MENSAJE_DESMARCACION_EXITOSA='Desmarcacion como favorito exitoso'

FAVORITO_MENSAJE_PDI_YA_SE_ENCUENTRA_MARCADO='El PDI que intenta marcar, ya se encuentra marcado'
FAVORITO_MENSAJE_PDI_NO_SE_ENCUENTRA_MARCADO='El PDI que intenta desmarcar, no se encuentra marcado'
