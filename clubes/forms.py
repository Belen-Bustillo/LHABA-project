from django import forms
from clubes.models import ClubesRegistrados

class ClubesRegistradosForm(forms.ModelForm):
    class Meta:
        model = ClubesRegistrados
        fields = ("nombre_siglas","nombre_completo","nombre_corto","localidad","email")
        widgets = {
            "nombre_siglas": forms.TextInput(attrs={'class':'form-control'}),
            "nombre_completo": forms.TextInput(attrs={'class':'form-control'}),
            "nombre_corto": forms.TextInput(attrs={'class':'form-control'}),
            "localidad": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
        }
