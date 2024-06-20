from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from . import forms


class HomeView(TemplateView):
  template_name = "accounts/home.html"


class LoginView(LoginView):
  form_class = forms.LoginForm
  template_name = "accounts/login.html"


class LogoutView(LogoutView):
  pass


class SignUpView(CreateView):
  form_class = forms.SignUpForm
  template_name = "accounts/signup.html"
  success_url = reverse_lazy("accounts:home")

  def form_valid(self, form):
    response = super().form_valid(form)
    login_id = form.cleaned_data.get("login_id")
    password = form.cleaned_data.get("password1")
    user = authenticate(login_id=login_id, password=password)
    login(self.request, user)
    return response
