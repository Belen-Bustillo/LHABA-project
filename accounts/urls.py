from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *

urlpatterns = [
    path("registrarse/",Register.as_view(), name="register"),
    path("perfil_coordinador/",ProfileDetailView.as_view(), name="profile_detail"),
    path("perfil_coordinador/modificar/",ProfileChange.as_view(), name="profile_change"),
    path("login/",Login.as_view(), name="login"),
    path("logout/",Logout.as_view(), name="logout"),
    path("perfil_coordinador/pass_change/",UserPasswordChangeView.as_view(), name="pass_change"),
]