from django.conf.urls import *
from views import *

urlpatterns = patterns(
    '',

    # main site
    url(r'^$', index, name='index'),

    # RegistroOE
    url(r'^registro-oe/$', registro_oe, name='registro_oe'),
    url(r'^registro-comite/$', registro_comite, name='registro_comite'),
    url(r'^registro-miembro/$', miembros_oe, name='registro_miembro'),
    url(r'^registro-bancario/$', datos_bancarios, name='registro_bancario'),
    url(r'^directorio/$', directorio, name='directorio'),
    url(r'^directorio/(?P<oe_slug>[\w-]+)/$', perfil_oe, name='perfil_oe'),
)
