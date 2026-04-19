from django.shortcuts import render, get_object_or_404
from clubes.models import ClubesRegistrados

# Create your views here.
def home(request):
    return render(request, "clubes/index.html")

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