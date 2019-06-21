from django import forms
from Apps.gestionTrabajadores.models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = [
            'dni',
            'apellidos',
            'nombres',
            'pais',
            'fechaNacimiento',
            'foto',
        ]
        labels = {
            'dni':'DNI',
            'apellidos':'Apellidos',
            'nombres':'Nombres',
            'pais':'País',
            'fechaNacimiento':'Fecha de Nacimiento',
            'foto':'Foto',
        }
        widgets = {
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.Select(attrs={'class':'form-control'}),
            'fechaNacimiento':forms.TextInput(attrs={'class':'form-control','data-provide':'datepicker'}),

        }
