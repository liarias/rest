from .models import *
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = "__all__"

class ServicioUsuarioSerializer(serializers.ModelSerializer):
	servicio = ServicioSerializer()
	
	class Meta:
		model = Persona
		fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):
	servicios = ServicioUsuarioSerializer(many=True)
	
	class Meta:
		model = Persona
		fields = "__all__"

