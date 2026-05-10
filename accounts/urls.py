from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
from clubes.views import registrar_club, actualizar_club,registrar_persona, ver_equipos_admin

urlpatterns = [
    path("registrarse/",Register.as_view(), name="register"),
    path("perfil_coordinador/",ProfileDetailView.as_view(), name="profile_detail"),
    path("perfil_coordinador/modificar/",ProfileChange.as_view(), name="profile_change"),
    path("login/",Login.as_view(), name="login"),
    path("logout/",Logout.as_view(), name="logout"),
    path("perfil_coordinador/pass_change/",UserPasswordChangeView.as_view(), name="pass_change"),
    path("perfil_coordinador/crear_club/", registrar_club, name="registrar_club"),
    path("perfil_coordinador/<nombre_siglas>/actualizar/", actualizar_club, name="club_actualizar"),
    path("perfil_coordinador/<nombre_siglas>/equipos/registrar_persona/", registrar_persona, name="registrar_persona"),
    path("perfil_coordinador/<nombre_siglas>/equipos/ver/", ver_equipos_admin, name="ver_equipos"),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)