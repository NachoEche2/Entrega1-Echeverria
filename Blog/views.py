from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Pais, Transporte, Autor
from Blog.forms import PaisFormulario
# Create your views here.


def inicio (request):
    transporte = Transporte (
        clase ="Avion", costo = 1000
    )
    transporte.save()
    contexto = {"transporte-1": transporte}
    return render(request, "Blog/inicio.html", contexto)

def inicio (request):
    autor = Autor (
        nombre ="Luis", apellido = "Perez", profesion = "doctor"
    )
    autor.save()
    contexto = {"autor-1": autor}
    return render(request, "Blog/inicio.html", contexto)

def autor (request):
    return render (request,"Blog/autor.html")

def pais(request):
    return render (request,"Blog/pais.html")

def transporte(request):
    return render (request,"Blog/transporte.html")


def procesar_formulario2(request):
    if request.method != "POST":
        mi_formulario = PaisFormulario()
    else:
        mi_formulario = PaisFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            pais = Pais(nombre=informacion["pais"], satisfaccion=informacion["satisfaccion"], ciudad_visitada=informacion ["ciudad_visitada"])
            pais.save()
            return render(request,"Blog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "Blog/formulario-2.html", contexto)

def busqueda(request):
    return render(request, "Blog/busqueda.html")

def busqueda_2(request):
    return render(request, "Blog/busqueda-2.html")

def buscar(request):
    respuesta = f"Buscando el pais : {request.GET['pais']}"
    return HttpResponse(respuesta)  

def buscar_2(request):
    
    if not request.GET["pais"]:
        return HttpResponse("No enviaste datos")
    else:
        pais_a_buscar = request.GET["pais"]
        pais = Pais.objects.filter(pais=pais_a_buscar)

        contexto = {"pais": pais_a_buscar, "pais_encontrados": pais}

        return render(request, "Blog/resultado_busqueda.html", contexto)

def entregables(request):
    return render(request, "Blog/entregables.html")


from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

class PaisList(ListView):
    model = Pais
    template_name = "Blog/pais-list.html"
    
class PaisDetalle(DetailView):
    model = Pais
    template_name = "Blog/pais-detalle.html"
    
from django.urls import reverse
    
class PaisCreacion(CreateView):
    model = Pais
    success_name = "/Blog/pais/list.html"
    fields = ["nombre", "satisfaccion","ciudad_visitada"]

    def get_success_url(self):
        return reverse("paisList")
    
class PaisUpdateView(UpdateView):
    model = Pais
    success_url = "/Blog/pais/list"
    fields = ["nombre", "satisfaccion","ciudad_visitada"]


class PaisDelete(DeleteView):
    model = Pais
    success_url = "/Blog/pais/list"
    
def busqueda_de_pais(request):
    return render(request, "Blog/busqueda_de_pais.html")


def buscar_curso(request):
    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        pais = Pais.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "pais_encontrados": pais}

        return render(request, "Blog/resultado_busqueda_nombre.html", contexto)

