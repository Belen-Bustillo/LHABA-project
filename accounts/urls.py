from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *

urlpatterns = [
    path("registrarse/",Register.as_view(), name="register"),
    path("perfil_coordinador/",ProfileDetailView.as_view(), name="profile_detail"),
    path("perfil_coordinador/modificar/",ProfileChange.as_view(), name="profile_change"),
    path("login/",Login.as_view(), name="login"),
    path("logout/",Logout.as_view(), name="logout"),
    path("perfil_coordinador/pass_change/",UserPasswordChangeView.as_view(), name="pass_change"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)