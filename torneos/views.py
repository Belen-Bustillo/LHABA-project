from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from torneos.models import *
from clubes.models import ClubesRegistrados, Categoria
from datetime import date
from accounts.views import es_coordinador
from clubes.models import PersonaRol

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

@login_required
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

@login_required
def registrar_participacion_torneo(request, torneo_id, club_id, categoria_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)
    club = get_object_or_404(ClubesRegistrados, id=club_id)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

    # seguridad: validar categoría
    if torneo.categoria != categoria:
        return redirect("torneos_listar")

    existe = ParticipacionTorneo.objects.filter(
        torneo=torneo,
        club=club
    ).exists()

    if existe:
        return redirect("torneo_detail", torneo_id=torneo.torneo_id)

    ParticipacionTorneo.objects.create(
        torneo=torneo,
        club=club,
        categoria=categoria
    )

    return redirect(
        "torneo_confirmacion",
        torneo_id=torneo.id,
        club_id=club.id
    )

@login_required
def seleccionar_torneo(request, club_id, categoria_id):
    club = get_object_or_404(ClubesRegistrados, id=club_id)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

    # torneos compatibles
    torneos = Torneo.objects.filter(
        categoria=categoria
    )

    contexto = {
        "club": club,
        "categoria": categoria,
        "torneos": torneos
    }

    return render(request, "torneos/torneo_seleccionar.html", contexto)

@login_required
def torneo_confirmacion(request, torneo_id, club_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)
    club = get_object_or_404(ClubesRegistrados, id=club_id)

    return render(request, "torneos/torneo_confirmacion.html", {
        "torneo": torneo,
        "club": club
    })

@login_required
def mis_torneos(request, nombre_siglas):

    # club = get_object_or_404(
    #     ClubesRegistrados,
    #     nombre_siglas=nombre_siglas
    # )
    club = request.user.club

    if not es_coordinador(club, request.user):
        return redirect("home")

    participaciones = ParticipacionTorneo.objects.filter(
        club=club
    ).select_related("torneo", "categoria")

    categorias_ids = PersonaRol.objects.filter(
        club=club
    ).values_list(
        "categoria",
        flat=True
    ).distinct()

    categorias = Categoria.objects.filter(
        id_categoria__in=categorias_ids
    )

    torneos_disponibles = Torneo.objects.filter(
        categoria__id_categoria__in=categorias_ids
    )

    categorias = Categoria.objects.filter(
        id_categoria__in=categorias_ids
    )
    
    participaciones_ids = ParticipacionTorneo.objects.filter(
        club=club
    ).values_list(
        "torneo_id",
        flat=True
    )    

    contexto = {
        "club": club,
        "participaciones": participaciones,
        "torneos_disponibles": torneos_disponibles,
        "participaciones_ids": participaciones_ids,
        "categorias": categorias,
        "hoy": date.today()
    }
    return render(
        request,
        "torneos/torneos_administrar.html",
        contexto
    )

@login_required
def confirmar_inscripcion(request, torneo_id, club_id, categoria_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)
    club = get_object_or_404(ClubesRegistrados, id=club_id)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

    return render(request, "torneos/torneo_confirmacion.html", {
        "torneo": torneo,
        "club": club,
        "categoria": categoria
    })

@login_required
def inscribir_en_torneo(request, torneo_id, club_id, categoria_id):

    torneo = get_object_or_404(Torneo, torneo_id=torneo_id)
    club = get_object_or_404(ClubesRegistrados, id=club_id)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

    if request.method != "POST":
        return redirect("confirmar_inscripcion", torneo_id=torneo_id, club_id=club_id, categoria_id=categoria_id)

    # evitar duplicados
    existe = ParticipacionTorneo.objects.filter(
        torneo=torneo,
        club=club,
        categoria=categoria
    ).exists()

    if existe:
        return redirect("mis_torneos", nombre_siglas=club.nombre_siglas)

    ParticipacionTorneo.objects.create(
        torneo=torneo,
        club=club,
        categoria=categoria
    )

    return redirect("torneo_confirmacion", torneo_id=torneo_id, club_id=club_id)