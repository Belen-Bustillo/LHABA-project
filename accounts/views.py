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
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import *
from accounts.forms import *

# def register(request):
#     if request.method == "POST":
#         form = ProfileCreateForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("profile_detail")
#     else:
#         form = PerfilCreateForm()
#     return render(request, "accounts/register.html", {"form": form})


class Register(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)  # guarda el usuario
        login(self.request, self.object)     # this.object = user creado
        return response
    
class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = self.request.user
    #     return context
