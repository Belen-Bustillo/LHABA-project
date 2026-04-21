from django.db import models

class ClubesRegistrados(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_siglas = models.CharField()
    nombre_completo = models.CharField()
    nombre_corto = models.CharField(max_length=30,null=True)
    localidad = models.CharField()
    email = models.EmailField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Club registrado: {self.nombre_siglas} - {self.nombre_completo}"

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return f"Categoria creada: {self.nombre_categoria}"

class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Persona registrada: {self.nombre} {self.apellido}"
    
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    rol = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80,null=True)
    
    def __str__(self):
        if self.descripcion:
            mensaje = f"Rol definido: {self.rol} - {self.descripcion}"
        else:
            mensaje = f"Rol definido: {self.rol}"
        return mensaje

class PersonaRol(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) #id_persona
    club = models.ForeignKey(ClubesRegistrados, on_delete=models.CASCADE) #id (club)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT) #id_rol
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT) #id_categoria
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_cambio = models.DateField(null=True)

    def __str__(self):
        return f"Se añadio a {self.persona.nombre} {self.persona.apellido} \nclub {self.club.nombre_siglas} \nrol de {self.rol.rol} \ncategoria {self.categoria.nombre_categoria}"

# class Fixture(models.Model):
#     pass
    

# class Torneos(models.Model):
    # pass