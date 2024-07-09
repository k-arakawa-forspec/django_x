from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from . import forms

# 24/6/20課題により追加
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post

class HomeView(TemplateView):
  template_name = "accounts/home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.all()
    context["post_list"] = post_list
    return context

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

# 24/6/20課題により追加
class MyListView(LoginRequiredMixin ,ListView):
  """自分の投稿のみ表示"""
  model = Post
  template_name = "accounts/home.html"
  # template_name = "accounts/mylist.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    mypost_list = Post.objects.filter(user=self.request.user)
    #.order_by('-id')
    context["post_list"] = mypost_list
    return context