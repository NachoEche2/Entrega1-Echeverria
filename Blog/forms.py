from django import forms

class PaisFormulario(forms.Form):
    pais = forms.CharField()
    fechaSalida = forms.DateField()