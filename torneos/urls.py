from django.urls import path
from torneos.views import *

urlpatterns = [
    path("torneos/", torneos_listar,name="torneos_listar"),
    path("torneos/<str:torneo_id>/", torneo_detail, name="torneo_detail"),
]