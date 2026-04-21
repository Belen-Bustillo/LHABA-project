from django.shortcuts import render, get_object_or_404, redirect
from clubes.models import *
from clubes.forms import ClubesRegistradosForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def clubes_list(request):
    clubes_query = ClubesRegistrados.objects.all()
    contexto = {
        "clubes_list" : list(clubes_query)
    }
    return render(request, "clubes/clubes_list.html", contexto)

def club_detalle(request,id):
    club = get_object_or_404(ClubesRegistrados, id=id)
    contexto = {
        "club" : club
    }
    return render(request, "clubes/club_detail.html", contexto)

def ver_equipos(request,id):
    club = get_object_or_404(ClubesRegistrados, id=id)
    categorias = Categoria.objects.all()
    personas = PersonaRol.objects.filter(club=club)

    equipos = []

    for categoria in categorias:
        ver_personas = personas.filter(categoria=categoria)
        dt = ver_personas.filter(rol__rol="Director Tecnico").first()
        asistentes = ver_personas.filter(rol__rol="Asistente")
        jugadoras = ver_personas.filter(rol__rol="Jugadora")

        if ver_personas.exists():
            lista_asistentes = []
            for a in asistentes:
                lista_asistentes.append(a.persona)

            lista_jugadoras = []
            for b in jugadoras:
                lista_jugadoras.append(b.persona)

            equipos.append({
                "categoria": categoria.nombre_categoria,
                "dt":dt.persona,
                "asistente":lista_asistentes,
                "jugadoras":lista_jugadoras
            })

    contexto = {
        "club": club,
        "equipos": equipos
    }

    return render(request, "clubes/equipo_detail.html", contexto)

def registrar_club(request):
    if request.method == "POST":
        form = ClubesRegistradosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clubes_list")
    else:
        form = ClubesRegistradosForm()
    contexto = {"form": form}
    return render(request, "clubes/club_create.html", contexto)
