from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Blog.models import Avatar


class PaisFormulario(forms.Form):

    pais = forms.CharField()
    satisfaccion = forms.IntegerField()
    ciudad_visitada = forms.CharField()
    itinerario = forms.CharField(widget=forms.Textarea)
    año=forms.IntegerField()



class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Primer Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        # help_texts = {k: "" for k in fields}

class AvatarForm(forms.ModelForm):

    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["user"]
