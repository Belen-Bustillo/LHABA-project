from django.shortcuts import render, get_object_or_404, redirect
from clubes.models import *
from clubes.forms import *

# Create your views here.
def home(request):
    return render(request, "index.html")


#READ
# clubes
def clubes_list(request):
    nombre = request.GET.get("search")
    clubes_query = ClubesRegistrados.objects.all()
    if nombre is not None:
        clubes_query = ClubesRegistrados.objects.filter(
            nombre_completo__icontains=nombre
        )
    contexto = {
        "clubes_list" : list(clubes_query)
    }
    return render(request, "clubes/clubes_list.html", contexto)

def club_detalle(request,nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    contexto = {
        "club" : club
    }
    return render(request, "clubes/club_detail.html", contexto)

#personas-equipos
def administrar_equipos(request,nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
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
                "categoria": categoria,
                "dt": dt.persona if dt else None,
                "asistentes": lista_asistentes,
                "jugadoras": lista_jugadoras
            })
 
    contexto = {
        "club": club,
        "equipos": equipos
    }
 
    return render(request, "clubes/equipo_administrar.html", contexto)

def ver_equipos_list(request,nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
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
                "categoria": categoria,
                "dt": dt.persona if dt else None,
                "asistentes": lista_asistentes,
                "jugadoras": lista_jugadoras
            })
 
    contexto = {
        "club": club,
        "equipos": equipos
    }
 
    return render(request, "clubes/equipo_detail_list.html", contexto)

#CREATE
#club
def registrar_club(request):
    if request.method == "POST":
        form = ClubesRegistradosForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.coordinador_deportivo = request.user
            club.save()
            return redirect("profile_detail")
    else:
        form = ClubesRegistradosForm()
    contexto = {"form": form}
    return render(request, "clubes/club_create.html", contexto)

#personas
def registrar_persona(request,nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)

    if request.method == "POST":
        persona_form = PersonaForm(request.POST)
        rol_form = PersonaRolForm(request.POST)

        if persona_form.is_valid() and rol_form.is_valid():
            # Guardar persona
            persona = persona_form.save()
            
            # Guardar PersonaRol
            persona_rol = rol_form.save(commit=False)
            persona_rol.persona = persona
            persona_rol.club = club
            persona_rol.save()
            
            return redirect("administrar_equipos", nombre_siglas=nombre_siglas)
    else:
        persona_form = PersonaForm()
        rol_form = PersonaRolForm()

    contexto = {
        "club": club,
        "persona_form": persona_form,
        "rol_form": rol_form
    }
    return render(request, "clubes/persona_registrar.html", contexto)

#UPDATE
#club
def actualizar_club(request, nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    if request.method == "POST":
        form = ClubesRegistradosForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = ClubesRegistradosForm(instance=club)      
    
    contexto = {
        "form" : form,
        "club" : club,
        "update" : True
    }
    return render(request, "clubes/club_update.html", contexto)

#personas
def actualizar_persona(request, nombre_siglas, persona_id):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    
    persona = get_object_or_404(Persona, id_persona=persona_id)
    persona_rol = get_object_or_404(PersonaRol, persona=persona, club=club)

    if request.method == "POST":
        persona_form = PersonaForm(request.POST, instance=persona)
        rol_form = PersonaRolForm(request.POST, instance=persona_rol)

        if persona_form.is_valid() and rol_form.is_valid():
            persona_form.save()
            rol_form.save()
            return redirect('administrar_equipos', nombre_siglas=nombre_siglas)

    else:
        persona_form = PersonaForm(instance=persona)
        rol_form = PersonaRolForm(instance=persona_rol)

    contexto = {
        "club": club,
        "persona_form": persona_form,
        "rol_form": rol_form
    }

    return render(request, "clubes/persona_actualizar.html", contexto)

#DELETE
#club
def consulta_eliminar_club(request, nombre_siglas):
    return render(request, "clubes/club_delete.html",{
        "nombre_siglas": nombre_siglas
    })

def eliminar_club(request, nombre_siglas):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    if request.method == "POST":
        club.delete()
        return redirect("profile_detail")

#personas-equipos
def consulta_eliminar_persona(request, nombre_siglas, persona_id):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    persona = get_object_or_404(Persona, id_persona=persona_id)
    return render(request, "clubes/persona_delete.html",{
        "club": club,
        "persona": persona
    })

def eliminar_persona(request, nombre_siglas, persona_id):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    persona = get_object_or_404(Persona, id_persona=persona_id)
    if request.method == "POST":
        persona.delete()
        return redirect("administrar_equipos", nombre_siglas=nombre_siglas)
    return redirect("consulta_eliminar_persona", nombre_siglas=nombre_siglas, persona_id=persona_id)
    
def consulta_eliminar_equipo(request, nombre_siglas, categoria_id):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    return render(request, "clubes/equipo_delete.html",{
        "club": club,
        "categoria": categoria
    })

def eliminar_equipo(request, nombre_siglas, categoria_id):
    club = get_object_or_404(ClubesRegistrados, nombre_siglas=nombre_siglas)
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)

    if request.method == "POST":
        PersonaRol.objects.filter(
            club=club,
            categoria=categoria
        ).delete()

        return redirect("administrar_equipos", nombre_siglas=club.nombre_siglas)

    return render(request, "clubes/confirmar_eliminar_equipo.html", {
        "club": club,
        "categoria": categoria
    })