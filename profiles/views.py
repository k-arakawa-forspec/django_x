 # 2024/07/18 課題
from django.urls import reverse_lazy
from . import forms
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.shortcuts import resolve_url


# モデルのインポート
from profiles.models import Profile


# Create your views here.
class OtherProfView(DetailView):
  # 自分以外のユーザーの投稿を表示
  model = Profile
  template_name = "profiles/prof.html"

  queryset = Profile.objects.select_related('user')

class MyProfView(DetailView):
  # 自分の投稿を表示
  model = Profile
  template_name = "profiles/myprof.html"

  def get_object(self, queryset=None):
    return Profile.objects.get(user_id = self.request.user.id)

class ProfileUpdateView(UpdateView):
  model = Profile
  template_name = "profiles/update.html"
  form_class = forms.ProfileUpdateForm
  success_url = reverse_lazy("profiles:myprof")
  
  def get_success_url(self):
    return resolve_url('profiles:myprof', pk=self.kwargs['pk'])

  # contextデータ作成
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["process_name"] = "Update"
    return context