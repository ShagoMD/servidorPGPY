from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from view_pdi import *
from view_usuario import *
from view_pdi_search import *
from view_pdi_search_category import *


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
 (r'^pdi/registrar/$', registrarPDI),
 (r'^pdi/lista/$', peticionObtenerListadoPuntosDeInteres),
 (r'^usuario/registrar/$',peticionRegistrarUsuario),
 (r'^pdi/buscar/$', peticionObtenerListadoPuntosDeInteresSearch),
 (r'^pdi/categoria/$', peticionObtenerListadoPuntosDeInteresSearchCategoria),
 
 #(r'^time/plus/(\d{1,2})/$', hours_ahead),


)
