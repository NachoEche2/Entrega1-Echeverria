"""ProyectoCoder2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from multiprocessing import context
from django.urls import path
from re import template

from Blog.views import (
    inicio,
    autor,
    pais,
    transporte,
    procesar_formulario2,
    busqueda,
    busqueda_2,
    buscar,
    buscar_2,
    entregables,
    PaisList,
    PaisDetalle,
    PaisCreacion,
    PaisUpdateView,
    PaisDelete,
    busqueda_de_pais,
    MyLogin,
    MyLogout,
    register,
    editar_perfil,
    agregar_avatar,
    listar_pais,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="Inicio"),
    path("autor/", autor, name="autor"),
    path("pais/", pais, name="pais"),
    path("transporte/", transporte, name="transporte"),
    path("formulario-2/", procesar_formulario2, name="formulario-2"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar/", buscar),
    path("buscar-2/", buscar_2),
    path("entregables/", entregables, name="entregables"),
    path("pais/list", PaisList.as_view(), name="paislist"),
    #path("r'(?P<pk>\d+)^$'", PaisDetalle.as_view(), name="PaisDetail"),
    path("pais-nuevo/", PaisCreacion.as_view(), name="PaisNew"),
    path("editar/<pk>", PaisUpdateView.as_view(), name="PaisUpdate"),
    path("borrar/<pk>", PaisDelete.as_view(), name="PaisDelete"),
    path("busqueda-de-pais/", busqueda_de_pais, name="busqueda"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    path("pais/<pk>'", PaisDetalle.as_view(), name="PaisDetail"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    path("Listar-lista/", listar_pais),
]



