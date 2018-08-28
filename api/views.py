from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from .models import *
import datetime
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView

def personas(request):
    personas = Persona.objects.all()
    response = render(request,'api/PersonasListar.html',{'personas':personas})
    return response

def PersonaDetalle(request,pk):
    persona = Persona.objects.get(pk=pk)
    response = render(request,'api/DetallePersona.html',{'persona':persona})
    return response

class ServicioListar(APIView):
	def get(self, request, format=None):
		servicio = Servicio.objects.all()
		serializer = ServicioSerializer(servicio, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = ServicioSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaListar(APIView):
    """
    Lista todos los usuarios o crea un nuevo usuario.
    """
    def get(self, request, format=None):
        usuario = Persona.objects.all()
        serializer = PersonaSerializer(usuario, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePersona(APIView):

    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = PersonaSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        servicio = Persona.objects.get(nombre=request.POST['servicio'])
        if not persona.servicios.filter(servicio=servicio):
            personaServicio = ServicioUsuario(persona=persona,servicio=servicio,fecha = datetime.datetime.strptime(request.POST['registro'],"%Y-%m-%d"),
                direccion=request.POST['direccion'])
            usuarioServicio.save() 
            serializer = PersonaSerializer(usuario)
            return Response(serializer.data)
        else:
            return Response("Ya esta registrado ese servicio", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DetalleServicioPersona(APIView):

    def get_object(self, pk):
        try:
            return ServicioPersona.objects.get(pk=pk)
        except ServicioPersona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = ServicioPersonaSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        servicio = ServicioPersona.objects.get(nombre=request.POST['servicio'])
        if not persona.servicios.filter(servicio=servicio):
            personaServicio = ServicioUsuario(persona=persona,servicio=servicio,fecha = datetime.datetime.strptime(request.POST['registro'],"%Y-%m-%d"),
                direccion=request.POST['direccion'])
            usuarioServicio.save() 
            serializer = PersonaSerializer(usuario)
            return Response(serializer.data)
        else:
            return Response("Ya esta registrado ese servicio", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)