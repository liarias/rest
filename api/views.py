from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def personas(request):
    personas = Persona.objects.all()
    response = render(request,'api/PersonasListar.html',{'personas':personas})
    return response


def PersonaDetalle(request,pk):
    persona = Persona.objects.get(pk=pk)
    response = render(request,'api/DetallePersona.html',{'persona':persona})
    return response

def servicios(request):
    servicios = Servicio.objects.all()
    response = render(request,'api/PersonasListar.html',{'servicios':servicios})
    return response


def ServicioDetalle(request,pk):
    servicio = Servicio.objects.get(pk=pk)
    response = render(request,'api/DetalleServicio.html',{'servicio':servicio})
    return response

def ServicioPersonaDetalle(request,pk):
    print("entra")
    servicioPersona = ServicioPersona.objects.get(pk=pk)
    print(servicioPersona.persona.nombre)
    response = render(request,'api/DetalleServicio.html',{'servicioPersona':servicioPersona})
    return response

def nuevoServicio(request,pk):
    persona = Persona.objects.get(pk=pk)
    response = render(request,'api/nuevoServicio.html',{'persona':persona})
    return response

class ServicioListar(APIView):
    def get(self, request, format=None):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        print(serializer.data)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleServicio(APIView):

    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        servicio = self.get_object(pk)
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        servicio = self.get_object(pk)
        serializer = ServicioSerializer(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        servicio = self.get_object(pk)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ServicioPersonaListar(APIView):
    """
    Lista todos los usuarios o crea un nuevo usuario.
    """
    def get(self, request, format=None):
        servicioPersona = ServicioPersona.objects.all()
        serializer = ServicioPersonaSerializer(servicioPersona, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("entra")
        serializer = ServicioPersonaSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleServicioPersona(APIView):

    def get_object(self, pk):
        try:
            return ServicioPersona.objects.get(pk=pk)
        except ServicioPersona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        servicioPersona = self.get_object(pk)
        serializer = ServicioPersonaSerializer(servicioPersona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print("entra put")
        servicioPersona = self.get_object(pk)
        print(request.data)
        serializer = ServicioPersonaSerializer(servicioPersona, data=request.data)
        print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        servicioPersona = self.get_object(pk)
        servicioPersona.delete()
        redirect("api/DetallePersona.html");
        return Response(status=status.HTTP_204_NO_CONTENT)