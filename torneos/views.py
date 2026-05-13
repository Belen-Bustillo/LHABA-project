from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from torneos.models import *
from clubes.models import ClubesRegistrados, Categoria
from datetime import date

#READ
def torneos_listar(request):
    torneos = Torneo.objects.all()
    contexto = {
        "torneos" : torneos
    }
    return render(request, "torneos/torneos_listar.html", contexto)

def torneo_detail(request, torneo_id):
    torneo = get_object_or_404(Torneo, torneo_id=torneo_id)

    participaciones = ParticipacionTorneo.objects.filter(
        torneo=torneo
    ).select_related("club", "categoria")

    contexto = {
        "torneo": torneo,
        "participaciones": participaciones,
        "hoy": date.today()
    }

    return render(request, "torneos/torneo_detail.html", contexto)

def registrar_participacion_torneo(request, torneo_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)
    clubes = ClubesRegistrados.objects.all()

    if request.method == "POST":
        club_id = request.POST.get("club")
        categoria_id = request.POST.get("categoria")

        club = get_object_or_404(ClubesRegistrados, id=club_id)
        categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

        # evitar duplicados
        existe = ParticipacionTorneo.objects.filter(
            torneo=torneo,
            club=club
        ).exists()

        if existe:
            messages.error(request, "Este club ya está inscripto en el torneo.")
            return redirect("registrar_participacion_torneo", torneo_id=torneo.id)

        ParticipacionTorneo.objects.create(
            torneo=torneo,
            club=club,
            categoria=categoria
        )

        return redirect("detalle_torneo", torneo_id=torneo.id)

    contexto = {
        "torneo": torneo,
        "clubes": clubes,
        "categorias": Categoria.objects.all()
    }

    return render(request, "torneos/torneo_registrar.html", contexto)
