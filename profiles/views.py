 # 2024/07/18 課題
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ListView

# モデルのインポート
from . import forms
from posts.models import Post
from profiles.models import Profile


# Create your views here.
class OtherProfView(ListView):
  model = Post
  template_name = "profiles/prof.html"

class MyProfView(ListView):
  model = Post
  template_name = "profiles/myprof.html"

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  model = Profile
  template_name = "profiles/update.html"
  form_class = forms.ProfileUpdateForm

