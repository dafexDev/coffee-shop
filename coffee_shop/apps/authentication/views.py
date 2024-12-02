from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    template_name = "auth/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("auth:login")
