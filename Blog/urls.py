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
from django.urls import path

from Blog.views import mostrar_inicio, mostrar_autor, mostrar_pais, mostrar_transporte, procesar_formulario2, busqueda,busqueda_2 ,buscar, buscar_2

urlpatterns = [
    path('inicio/', mostrar_inicio, name = "inicio"),
    path("autor/", mostrar_autor, name = "autor"),
    path("pais/", mostrar_pais, name = "pais"),
    path("transporte/", mostrar_transporte, name = "transporte"),
    path("formulario-2/", procesar_formulario2, name="formulario-2"),
    path("busqueda/", busqueda, name="busqueda"),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar/", buscar),
    path("buscar-2/", buscar_2),


]
