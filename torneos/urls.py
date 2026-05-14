from django.urls import path
from torneos.views import *

urlpatterns = [
    path("torneos/", torneos_listar,name="torneos_listar"),
    path("torneos/<str:torneo_id>/", torneo_detail, name="torneo_detail"),
    path("torneos/<str:torneo_id>/registrar/", registrar_participacion_torneo, name="torneo_registrar"),
    path("torneos/seleccionar/<int:club_id>/<int:categoria_id>/", seleccionar_torneo, name="seleccionar_torneo"),
    path("torneos/inscribir/<int:torneo_id>/<int:club_id>/<int:categoria_id>/", registrar_participacion_torneo, name="registrar_participacion_torneo"),
    path("torneos/confirmacion/", torneo_confirmacion, name="torneo_confirmacion"),
]


