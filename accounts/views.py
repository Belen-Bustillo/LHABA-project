from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import *
from accounts.forms import *
from clubes.models import Categoria

class Login(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("profile_detail")

class Register(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("profile_detail")

    def form_valid(self, form):
        response = super().form_valid(form)  # guarda el usuario
        login(self.request, self.object)     # this.object = user creado
        return response
    
class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, "club"):
            categorias = Categoria.objects.filter(
                personarol__club=user.club
            ).distinct()
            context["equipos"] = categorias
        else:
            context["equipos"] = []
        return context

class ProfileChange(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "accounts/profile_change.html"
    success_url = reverse_lazy("profile_detail")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):

        if self.request.POST.get("delete_avatar"):

            if self.object.avatar:
                self.object.avatar.delete(save=False)

            self.object.avatar = "default/avatar.png"

        return super().form_valid(form)
    
class Logout(LogoutView):
    next_page = reverse_lazy("home")

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/pass_change.html"
    success_url = reverse_lazy("profile_detail")