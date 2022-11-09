from django.test import TestCase
from django.test import TestCase
from Blog.models import Pais, Transporte
# Create your tests here.


class ViewTestCase(TestCase):

    def test_crear_pais(self):
        Pais.objects.create(nombre="test 1234", satisfaccion ="9091",ciudad_visitada ="Potosi")
        todos_los_pais = Pais.objects.all()
        assert len(todos_los_pais) == 1
        assert todos_los_pais[0].nombre == "test 1234"


    def test_crear_pais_sin_satisfaccion(self):
        Pais.objects.create(nombre="test 1234", satisfaccion ="9091",ciudad_visitada ="Potosi")
        todos_los_pais = Pais.objects.all()
        assert todos_los_pais[0].satisfaccion  is None


    def test_crear_transporte_sin_satisfaccion(self):
        Transporte.objects.create(nombre="test 1234", costo  ="9091",clase ="Tren")
        todos_los_transporte = Transporte.objects.all()
        assert todos_los_transporte[0].clase  is None