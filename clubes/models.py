from django.db import models

class ClubesRegistrados(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField()
    nombre_corto = models.CharField(max_length=30,null=True)
    localidad = models.CharField()
    email = models.EmailField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Club registrado: {self.id} - {self.nombre_completo}"
