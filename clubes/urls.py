from django.urls import path
from clubes.views import *

urlpatterns = [
         #url, funcion,nombre
    path("",home, name="home"),
    path("clubes",clubes_list,name="clubes_list"),
    path("clubes/<int:id>/", club_detalle, name="club_detalle"),
    path("clubes/<int:id>/equipos/", ver_equipos, name="equipos_detalle"),
    path("clubes/registrar/", registrar_club, name="registrar_club"),
    path("clubes/<int:id>/equipos/registrar_persona/", registrar_persona, name="registrar_persona"),
]
