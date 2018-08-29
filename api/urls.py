from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    path(r'', views.personas,name='personas'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.PersonaDetalle, name="personaDetalle"),
    url(r'^servicio/modificarServicio/(?P<pk>[0-9]+)/$', views.ServicioPersonaDetalle, name="ServicioDetalle"),
    url(r'^servicio/crearServicio/(?P<pk>[0-9]+)/$', views.nuevoServicio,name="servicioCrear"),
    url(r'^api/cargarServicios/$', views.ServicioListar.as_view()),
    url(r'^api/guardarServicio/$', views.ServicioPersonaListar.as_view()),
    url(r'^api/modificar/(?P<pk>[0-9]+)/$', views.DetalleServicioPersona.as_view()),
    url(r'^api/eliminar/(?P<pk>[0-9]+)/$', views.DetalleServicioPersona.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)