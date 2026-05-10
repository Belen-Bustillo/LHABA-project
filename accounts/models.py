from django.db import models
from django.contrib.auth.models import AbstractUser
# from clubes.models import ClubesRegistrados

def upload_avatar_path(instance, name):
    return f"avatars/{instance.username}/{name}"

class Profile(AbstractUser):
    avatar = models.ImageField(
        upload_to=upload_avatar_path,
        default="default/avatar.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    fecha_de_nacimiento = models.DateField(null=True)
    dni = models.CharField(max_length=15, unique=True)
    # club = models.OneToOneField(
    #     "clubes.ClubesRegistrados",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="coordinadores"
    # )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"