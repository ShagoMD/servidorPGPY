from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from view_pdi import *
from view_usuario import *
from view_pdi_search import *
from view_pdi_search_category import *
from view_categoria import *
from view_anuncio import *
from view_imagen import *
from view_Favorito import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', direct_to_template,{"template": "PDI/registrar_poi.html"}),
    #url(r'^$', direct_to_template,{"template": "PDI/registrar_usuario.html"}),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 (r'^pdi/registrar/$', peticionRegistrarPDI),
 (r'^pdi/actualizar/$', peticionActualizarPDI),
 (r'^pdi/eliminar/$', peticionEliminarPDI),
 (r'^pdi/eliminarTodo/$', peticionEliminarTodosPDI),
 (r'^pdi/lista/$', peticionObtenerListadoPuntosDeInteres),
 (r'^usuario/registrar/$',peticionRegistrarUsuario),
 (r'^usuario/iniciarSesion/$',peticionIniciarSesion),
 (r'^usuario/actualizar/$',peticionActualizarDatosDelPerfil),
 (r'^usuario/listapdi/$',peticionObtenerPDIsDeUsuario),
 (r'^usuario/listafavoritos/$',peticionObtenerFavoritosDeUsuario),
 (r'^usuario/perfil/$',peticionObtenerPerfilDeUsuario),
 (r'^pdi/buscar/$', peticionObtenerListadoPuntosDeInteresSearch),
 (r'^pdi/categoria/$', peticionObtenerListadoPuntosDeInteresSearchCategoria),
 (r'^categoria/registrar/$', peticionRegistrarCategoria),
 (r'^categoria/eliminar/$', peticionEliminarCategoria),
 (r'^categoria/actualizar/$', peticionActualizarCategoria),
 (r'^anuncio/registrar/$', peticionRegistrarAnuncio),
 (r'^anuncio/modificar/$', peticionModificarAnuncio),
 (r'^anuncio/eliminar/$', peticionEliminarAnuncio),
 (r'^anuncio/eliminarTodo/$', peticionEliminarTodoLosAnuncios), 
 (r'^anuncio/obtenerTodo/$', peticionObtenerTodosLosAnunciosDelPDI),
 (r'^favorito/marcar/$', peticionMarcarPDIcomoFavorito),
 (r'^imagen/mostrar/$', peticionImagen),
 (r'^imagen/eliminarTodo/$', peticionEliminarTodasLasImagenes),
 (r'^favorito/esfavorito/$',peticionEsPDIFavoritoDelUsuario),
 #(r'^time/plus/(\d{1,2})/$', hours_ahead),


)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
