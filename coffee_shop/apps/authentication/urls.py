from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path

from .views import RegisterView


app_name = "auth"


urlpatterns = [
    re_path(r"^login/$", LoginView.as_view(template_name="auth/login.html"), name="login"),
    re_path(r"^register/$", RegisterView.as_view(), name="register"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout")
]
