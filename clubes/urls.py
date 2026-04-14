from django.urls import path
from clubes.views import *

urlpatterns = [
         #url, funcion,nombre
    path("",home, name="home")
]
