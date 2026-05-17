from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
from clubes.views import (
    registrar_club, 
    actualizar_club,
    registrar_persona, 
    administrar_equipos, 
    actualizar_persona, 
    consulta_eliminar_persona,
    eliminar_persona,
    consulta_eliminar_club,
    eliminar_club,
    consulta_eliminar_equipo,
    eliminar_equipo
)
from torneos.views import (
    mis_torneos,
    confirmar_inscripcion,
    inscribir_en_torneo
)

urlpatterns = [
    #acciones propias de la cuenta
    path("registrarse/",Register.as_view(), name="register"),
    path("perfil_coordinador/",ProfileDetailView.as_view(), name="profile_detail"),
    path("perfil_coordinador/modificar/",ProfileChange.as_view(), name="profile_change"),
    path("login/",Login.as_view(), name="login"),
    path("logout/",Logout.as_view(), name="logout"),
    path("perfil_coordinador/pass_change/",UserPasswordChangeView.as_view(), name="pass_change"),

    #acciones para club
    path("perfil_coordinador/crear_club/", registrar_club, name="registrar_club"),
    path("perfil_coordinador/<nombre_siglas>/actualizar/", actualizar_club, name="club_actualizar"),
    path("perfil_coordinador/<nombre_siglas>/eliminar/", eliminar_club, name="eliminar_club"),
    path("perfil_coordinador/<nombre_siglas>/consulta_eliminar_club/", consulta_eliminar_club, name="consulta_eliminar_club"),

    #acciones para equipos-personas
    path("perfil_coordinador/<nombre_siglas>/equipos/administrar_equipos/", administrar_equipos, name="administrar_equipos"),
    path("perfil_coordinador/<nombre_siglas>/equipos/registrar_persona/", registrar_persona, name="registrar_persona"),
    path("perfil_coordinador/<nombre_siglas>/equipos/actualizar_persona/<int:persona_id>/", actualizar_persona, name="actualizar_persona"),
    path("perfil_coordinador/<nombre_siglas>/equipos/consulta_eliminar_persona/<int:persona_id>/",consulta_eliminar_persona, name ="consulta_eliminar_persona"),
    path("perfil_coordinador/<nombre_siglas>/equipos/eliminar_persona/<int:persona_id>/",eliminar_persona, name ="eliminar_persona"),
    path("perfil_coordinador/<nombre_siglas>/equipos/consulta_eliminar_equipo/<int:categoria_id>/", consulta_eliminar_equipo, name="consulta_eliminar_equipo"),
    path("perfil_coordinador/<nombre_siglas>/equipos/eliminar_equipo/<int:categoria_id>/", eliminar_equipo, name="eliminar_equipo"),

    #acciones para torneos
    path("perfil_coordinador/<nombre_siglas>/mis_torneos/",mis_torneos,name="mis_torneos"),
    path("perfil_coordinador/mis_torneos/inscribir/<int:torneo_id>/<int:club_id>/<int:categoria_id>/",inscribir_en_torneo,name="inscribir_en_torneo"),
    path("perfil_coordinador/mis_torneos/confirmar/<int:torneo_id>/<int:club_id>/<int:categoria_id>/",confirmar_inscripcion,name="confirmar_inscripcion"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)