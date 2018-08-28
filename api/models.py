from django.db import models

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	
class ServicioPersona(models.Model):
    persona = models.ForeignKey('Persona',related_name="servicios", on_delete=models.CASCADE)
    servicio = models.ForeignKey('Servicio',related_name="usuarios", on_delete=models.CASCADE)
    fecha = models.DateField()
    pago  = models.FloatField(null=True)
    ciudad = models.CharField(max_length=75)
    direccion = models.CharField(max_length=100)