from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import *

class ProfileCreateForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("username","first_name","last_name", "email", "dni","fecha_de_nacimiento")

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ("avatar","fecha_de_nacimiento","dni","first_name","last_name", "email","password")
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"class": "form-control","type": "date"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Profile
        fields = ("old_password", "new_password1", "new_password2")

    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )