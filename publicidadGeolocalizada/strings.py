# -*- encoding: utf-8 -*-
#La línea de arriba es para que python reconosca el ascii de las letras con acento

#En esta seccion se colocan Strings generales que pueden ser usados por cualquier View y/o api
GENERAL_MENSAJE_ERROR_TIPO_PETICION='La peticion no fue realizada a traves de POST.';
GENERAL_MENSAJE_CAMPO_TEXTO_INVALIDO="El campo de texto es invalido.";
GENERAL_MENSAJE_PARAMETROS_INCOMPLETOS='No se enviaron todos los parametros obligatorios.';
GENERAL_MENSAJE_PARAMETROS_INCORRECTOS='Los parametros son incorrectos.'


#En esta seccion se definen los strings usados por el View, la api y cualquier otra clase referente a PDI
PDI_MENSAJE_REGISTRO_EXITOSO='Registro de PDI exitoso';
PDI_MENSAJE_REGISTRO_FALLIDO='Ocurrio un error al intentar registrar el PDI. Intentelo de nuevo.';
PDI_MENSAJE_LOCALIZACION_REPETIDA='Los datos de localizacion del PDI que se desea registrar ya han sido utilizados previamente.';
PDI_MENSAJE_LIMITE_PDI_ALCANZADO='Se ha alcanzado el limite de PDI que su cuenta le permite registrar.';
PDI_MENSAJE_USUARIO_INVALIDO='El usuario no existe.';
PDI_MENSAJE_CATEGORIA_INVALIDA='La categoria sobre la cual se intenta registrar el PDI no existe.';

PDI_MENSAJE_URL_WEB_INVALIDA="La url del sitio web no tiene el formato correcto.";
PDI_MENSAJE_URL_IMAGEN_INVALIDA="La url de la imagen no tiene el formato correcto.";
PDI_MENSAJE_CORREO_INVALIDO="El correo electronico del sitio no es valido.";

PDI_MENSAJE_PDI_NO_EXISTE="El punto de interes no existe.";
PDI_MENSAJE_NO_HAY_PDIs_REGISTRADOS="El usuario no tiene puntos de interes registrados.";
PDI_MENSAJE_PDI_ELIMINADO="El punto de interes y todos sus anuncion asociados fueron eliminados correctamente.";
PDI_MENSAJE_TODOS_PDIS_ELIMINADOS="Todos los puntos de interes del usuario y sus respectivos anuncios han sido eliminados correctamente.";


PDI_MENSAJE_PARAMETRO_USUARIO_INVALIDO="El usuario debe ser un correo electronico.";
PDI_MENSAJE_PARAMETRO_PDI_INVALIDO="La referencia al pdi que intenta actualizar no posee un formato valido.";

PDI_MENSAJE_PARAMETRO_NOMBRE_PDI_INVALIDO="El nombre del pdi no tiene el formato valido.";
PDI_MENSAJE_PARAMETRO_CATEGORIA_INVALIDO="La categoria no tiene el formato valido.";
PDI_MENSAJE_PARAMETRO_LOCALIZACION_INVALIDO="Los datos de localizacion no tienen el formato valido.";
PDI_MENSAJE_PARAMETRO_DESCRIPCION_INVALIDO="La descripcion no puede tener solo espacios en blanco.";
PDI_MENSAJE_PARAMETRO_DIRECCION_INVALIDO="La direccion no puede tener solo espacios en blanco";
PDI_MENSAJE_PARAMETRO_TELEFONO_INVALIDO="No se pueden introducir espacios en blanco o letras en el telefono.";
PDI_MENSAJE_PARAMETRO_CORREO_INVALIDO="El correo electronico no tiene el formato adecuado";
PDI_MENSAJE_PARAMETRO_URL_INVALIDO="La url del sitio no tiene el formto adecuado";

PDI_MENSAJE_PDI_ACTUALIZADO="Los datos del punto de interes fueron actualizados correctamente.";
PDI_MENSAJE_PDI_NO_ACTUALIZADO="Los datos del PDI no pudieron ser actualizados. Intentelo de nuevo.";
PDI_MENSAJE_NO_PERTENECE_USUARIO="Este usuario no tiene los privilegios para modificar el PDI.";
PDI_MENSAJE_LISTA_OBTENIDA="Se ha obtenido correcatmente la lista de PDIs del usuario.";
PDI_MENSAJE_LISTA_FAVORITOS_OBTENIDA="Se ha obtenido correctamente la lista de Favoritos del usuario.";

#En esta seccion se definen los strings usados por el View, la api y otras clases correspondientes a Usuario
USUARIO_MENSAJE_CORREO_INVALIDO='Introduzca un correo electronico valido.';
USUARIO_MENSAJE_CONTRASENIA_INVALIDA='La contrasenia debe tener al menos 8 caracteres, una minuscula, una mayuscula y un digito.';
USUARIO_MENSAJE_CORREO_REPETIDO='El correo electronico introducido ya ha sido registrado en el sistema.';
USUARIO_MENSAJE_ERROR_INICIO_SESION="La combinacion de usuario y contrasenia utilizada no es valida.";
USUARIO_MENSAJE_INICIO_SESION_EXITOSO="Se ha iniciado sesion correctamente";
USUARIO_MENSAJE_USUARIO_NO_EXISTE="El usuario con el que trata de ingresar no existe.";
USUARIO_MENSAJE_ACTUALIZACION_VACIA='La actualizacion de los datos del perfil no sufrieron cambio alguno.';
USUARIO_MENSAJE_ID_DEL_USUARIO_INVALIDO='El ID del usuario es invalido.';
USUARIO_MENSAJE_ACTUALIZACION_EXISTOSA='Actualizacion de los datos del perfil exitoso.';
USUARIO_MENSAJE_ACTUALIZACION_FALLIDA='Actualizacion de los datos del perfil fallido.';
USUARIO_MENSAJE_REGISTRO_EXITOSO="El usuario fue registrado correctamente.";


#En esta seccion se definen los strings usados por el View, la api y otras clases concernientes a Categoria
CATEGORIA_MENSAJE_CATEGORIA_INVALIDA="El valor que trata de registrar no es unca cadena de texto.";
CATEGORIA_MENSAJE_CATEGORIA_VACIA="El nombre de la Categoria se encuentra vacio.";
CATEGORIA_MENSAJE_REGISTRO_EXITOSO="La categoria se registro exitosamente.";
CATEGORIA_MENSAJE_CATEGORIA_DUPLICADA="La categoria que intenta registrar ya existe.";
CATEGORIA_MENSAJE_CATEGORIA_ELIMINADA="La categoria fue eliminada.";
CATEGORIA_MENSAJE_PARAMETROS_VACIOS="Parametros vacios.";
CATEGORIA_MENSAJE_ID_INVALIDO="El id debe ser un entero.";
CATEGORIA_MENSAJE_NOMBRE_INVALIDO="El nombre debe ser una cadena de caracteres.";
CATEGORIA_MENSAJE_ERROR_ELIMINAR="No se pudo eliminar la categoria. Intentelo de nuevo.";
CATEGORIA_MENSAJE_CATEGORIA_NO_EXISTE="La categoria no existe.";
CATEGORIA_MENSAJE_NOMBRE_EXISTE="El nombre de la categoria que intenta actualizar ya existe";
CATEGORIA_MENSAJE_ACTUALIZADA="La categoria fue actualizada correctamente";
#En esta seccion se definen los strings usados por el View, la api, y otras clases relativas a Anuncio
ANUNCIO_MENSAJE_REGISTRO_EXITOSO='Registro del Anuncio exitoso.'
ANUNCIO_MENSAJE_REGISTRO_FALLIDO='Registro del Anuncio fallido.'

ANUNCIO_MENSAJE_ID_ANUNCIO_INVALIDO='Introdusca un id de Anuncio valido.'
ANUNCIO_MENSAJE_ID_PDI_INVALIDO='Introdusca un id de PDI valido.'
ANUNCIO_MENSAJE_CORREO_USER_INVALIDO='Introdusca un correo de Usuario valido.'
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
ANUNCIO_MENSAJE_ELIMINACION_EXITOSO='Eliminacion del anuncio exitoso.'

ANUNCIO_MENSAJE_ANUNCIO_ACTUALIZADO='Los datos del Anuncio de fueron actualizadas correctamente.'
ANUNCIO_MENSAJE_LIMITE_ANUNCIO_ALCANZADO='Se ha alcanzado el limite de Anuncios que su PDI le permite registrar.'
ANUNCIO_MENSAJE_TODOS_LOS_ANUNCIOS_EXITO='Todos los anuncios del PDI fueron devueltos correctamente.'

#En esta seccion se definen los strings usados por el View, la api, y otras clases relativas a Anuncio
FAVORITO_MENSAJE_MARCACION_EXITOSA='Marcacion como favorito exitoso.'
FAVORITO_MENSAJE_DESMARCACION_EXITOSA='Desmarcacion como favorito exitoso.'

FAVORITO_MENSAJE_CODIGO_MARCADO_INCORRECTO='El codigo para determinar si se marca o desmarca el PDI como favorito es incorrecto. Tiene que ser 0 para marcar y 1 para desmarcar'

FAVORITO_MENSAJE_PDI_YA_SE_ENCUENTRA_MARCADO='El PDI que intenta marcar, ya se encuentra marcado.'
FAVORITO_MENSAJE_PDI_NO_SE_ENCUENTRA_MARCADO='El PDI que intenta desmarcar, no se encuentra marcado.'

FAVORITO_MENSAJE_CODIGO_MARCADO_INVAIDO='El codigo para determinar si se marca o desmarca el PDI como favorito es invalido.'
FAVORITO_MENSAJE_CODIGO_NOTIFICACION_INVALIDO='El codigo para determinar si se desea recibir notificaciones de un PDI marcado como favorito es invalido.'
FAVORITO_MENSAJE_ES_FAVORITO="El pdi es un favorito del usuario";
FAVORITO_MENSAJE_NO_ES_FAVORITO="El pdi no es un favorito del usuario";
