from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *

urlpatterns = [
    path("registrarse/",Register.as_view(), name="register"),
    path("perfil_coordinador/",ProfileDetailView.as_view(), name="profile_detail")
]