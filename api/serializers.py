from .models import *
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = "__all__"

class ServicioPersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServicioPersona
		fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):
	servicios = ServicioPersonaSerializer(many=True)
	
	class Meta:
		model = Persona
		fields = "__all__"

