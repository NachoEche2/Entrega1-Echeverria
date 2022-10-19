from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path

from Blog.models import Pais, Transporte
from Blog.forms import PaisFormulario
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


def procesar_formulario2(request):
    if request.method != "POST":
        mi_formulario = PaisFormulario()
    else:
        mi_formulario = PaisFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            pais = Pais(nombre=informacion["pais"], fechaSalida=informacion["fechaSalida"])
            pais.save()
            return render(request, "Blog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "Blog/formulario-2.html", contexto)

def busqueda(request):
    return render(request, "Blog/busqueda.html")

def busqueda_2(request):
    return render(request, "Blog/busqueda_2.html")

def buscar(request):
    respuesta = f"Buscando el Pais : {request.GET['pais']}"
    return HttpResponse(respuesta)  # TODO: podríamos mostrarla, no?

def buscar_2(request):

    if not request.GET["pais"]:
        return HttpResponse("No enviaste datos")
    else:
        pais_a_buscar = request.GET["pais"]
        pais = Pais.objects.filter(pais=pais_a_buscar)

        contexto = {"pais": pais_a_buscar, "pais_encontrados": pais}

        return render(request, "Blog/resultado_busqueda.html", contexto)