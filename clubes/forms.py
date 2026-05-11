from django import forms
from clubes.models import ClubesRegistrados,Persona,PersonaRol

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

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ("nombre","apellido","dni","fecha_nacimiento","email")
        widgets = {
            "nombre": forms.TextInput(attrs={'class':'form-control'}),
            "apellido": forms.TextInput(attrs={'class':'form-control'}),
            "dni": forms.TextInput(attrs={'class':'form-control'}),
            "fecha_nacimiento": forms.DateInput(attrs={
                'class':'form-control',
                'type':'text',
                'placeholder':'dd/mm/aaaa'
            }),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #formato para que no tire error en fecha de nacimiento
        self.fields['fecha_nacimiento'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']


class PersonaRolForm(forms.ModelForm):
    class Meta:
        model = PersonaRol
        fields = ("categoria", "rol")
        widgets = {
            "categoria": forms.Select(attrs={'class':'form-control'}),
            "rol": forms.Select(attrs={'class':'form-control'}),
        }
