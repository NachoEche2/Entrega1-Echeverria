from django import forms


class PaisFormulario(forms.Form):
    
    pais = forms.CharField()
    satisfaccion = forms.IntegerField()
    ciudad_visitada=forms.CharField ()
    
