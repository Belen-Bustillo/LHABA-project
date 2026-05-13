from django.db import models
from clubes.models import Categoria,ClubesRegistrados

class Torneo(models.Model):
    id = models.AutoField(primary_key=True)
    torneo_id = models.CharField(max_length=20, unique=True, blank=True)
    temporada = models.CharField()
    nombre = models.CharField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    estado = models.CharField(default='Inactivo')
    def __str__(self):
        return f"{self.categoria} - {self.nombre} - {self.temporada}"
    
class ParticipacionTorneo(models.Model):
    torneo = models.ForeignKey(
        Torneo,
        on_delete=models.CASCADE
    )
    club = models.ForeignKey(
        ClubesRegistrados,
        on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)

    class Meta: 
        unique_together = ("torneo", "club")
    
    def __str__(self):
        return f"{self.torneo} - {self.club} - {self.categoria}"