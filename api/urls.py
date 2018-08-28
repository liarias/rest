from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include

from .views import *


urlpatterns = [
    path(r'', views.PersonaListar.as_view(),name='personas'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.PersonaDetalle, name="personaDetalle"),
    url(r'^servicio/nuevoServicio/(?P<pk>[0-9]+)/$', views.DetalleServicioPersona.as_view(), name="servicioCrear"),
    url(r'^servicio/crearServicio/$', views.ServicioListar.as_view()),
    url(r'^servicio/eliminar/(?P<pk>[0-9]+)/$', views.DetalleServicio.as_view(), name="eliminar"),

]

urlpatterns = format_suffix_patterns(urlpatterns)