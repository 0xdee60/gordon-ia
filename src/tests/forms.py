from django import forms
from django.forms import fields
from .models import User
class UsuarioCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nombres','apellidos','dni','fecha_nacimiento','sexo')
