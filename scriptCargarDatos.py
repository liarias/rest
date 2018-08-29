import csv
import os
from api.models import *
with open('todosmisservicios.csv',newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		lista = row[0].split(';')
		try:
			s=Servicio.objects.get(nombre=lista[1])
		except Servicio.DoesNotExist:
			s=Servicio()
			s.nombre = lista[1]
			s.save()
		try:
			p=Persona.objects.get(nombre=lista[0])
		except Persona.DoesNotExist:
			p = Persona()
			p.nombre = lista[0]
			p.save()		
		ps= ServicioPersona()
		ps.persona=p
		ps.servicio=s
		ps.ciudad = lista[2]
		ps.direccion = ''
		ps.fecha = lista[3]
		ps.pago = lista[4]
		ps.save()			