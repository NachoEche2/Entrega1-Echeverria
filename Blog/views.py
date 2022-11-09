from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Pais, Transporte, Autor, Avatar
from Blog.forms import PaisFormulario
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}
    return render(request, "Blog/inicio.html", contexto)

def autor(request):
    return render(request, "Blog/autor.html")

def pais(request):
    return render(request, "Blog/pais.html")

def transporte(request):
    return render(request, "Blog/transporte.html")


def procesar_formulario2(request):
    if request.method != "POST":
        mi_formulario = PaisFormulario()
    else:
        mi_formulario = PaisFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            pais = Pais(
                nombre=informacion["pais"],
                satisfaccion=informacion["satisfaccion"],
                ciudad_visitada=informacion["ciudad_visitada"],
            )
            pais.save()
            return render(request, "Blog/inicio.html")

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
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin


class PaisList(LoginRequiredMixin, ListView):
    
    model = Pais
    template_name = "Blog/pais-list.html"


@login_required
def listar_pais(request):
    todos_los_pais = Pais.objects.all()
    avatar = Avatar.objects.filter(user=request.user).first()
    contexto = {
        "pais_encontrados": todos_los_pais,
        "avatar": avatar.imagen.url
    }
    return render(request, "Blog/listar-pais.html", contexto)


class PaisDetalle(
    LoginRequiredMixin,
    DetailView,
):
    model = Pais
    template_name = "Blog/pais-detalle.html"


from django.urls import reverse


class PaisCreacion(LoginRequiredMixin, CreateView):
    model = Pais
    success_name = "/Blog/pais/list.html"
    fields = ["nombre", "satisfaccion", "ciudad_visitada"]

    def get_success_url(self):
        return reverse("paislist")


class PaisUpdateView(LoginRequiredMixin, UpdateView):
    model = Pais
    success_url = "/Blog/pais/list"
    fields = ["nombre", "satisfaccion", "ciudad_visitada"]


class PaisDelete(LoginRequiredMixin, DeleteView):
    model = Pais
    success_url = "/Blog/pais/list"


@login_required
def busqueda_de_pais(request):
    return render(request, "Blog/busqueda_de_pais.html")


@login_required
def buscar_pais(request):
    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        pais = Pais.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "pais_encontrados": pais}

        return render(request, "Blog/resultado_busqueda_nombre.html", contexto)


from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class MyLogin(LoginView):
    template_name = "Blog/login.html"


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "Blog/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/registro.html", {"form": form})

from Blog.forms import AvatarForm, UserEditionForm


@login_required
def editar_perfil(request):
    user = request.user
    if request.method == "POST":    #al presionar el botón

        form = UserEditionForm(request.POST) #el formulario es el del usuario

        if form.is_valid():

            data = form.cleaned_data     #info en modo diccionario

            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()


            return render(request, "Blog/inicio.html")

    else:

        form= UserEditionForm(initial={'username':user.username, 'email':user.email})

    return render(request, "Blog/editarPerfil.html",{'form':form, 'usuario':user.username})


@login_required
def agregar_avatar(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method != "POST":
        form = AvatarForm(initial={"email": user.email})
    else:
        form = AvatarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppCoder24/inicio.html", {"avatar": avatar.imagen.url})
        

        
    return render(request, "Blog/avatar_form.html",  {'form':form})
