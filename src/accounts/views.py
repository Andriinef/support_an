from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import CustomUserCreationForm


class RegistrationHomePageView(TemplateView):
    template_name = "registration/home.html"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
