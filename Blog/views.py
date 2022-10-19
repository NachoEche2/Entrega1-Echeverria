from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def mostrar_inicio (request):
    return HttpResponse ("Bienvenido Viajero")

def mostrar_inicio (request):
    return render (request,"Blog/inicio.html")

def mostrar_autor (request):
    return render (request,"Blog/autor.html")

def mostrar_pais(request):
    return render (request,"Blog/pais.html")

def mostrar_transporte(request):
    return render (request,"Blog/transporte.html")