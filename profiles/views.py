from . import forms
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.shortcuts import redirect, resolve_url


from profiles.models import Profile

class ProfView(DetailView):
  model = Profile
  template_name = "profiles/profiles.html"

  queryset = Profile.objects.select_related('user')

class MyProfView(DetailView):
  model = Profile
  template_name = "profiles/myprof.html"

  def get_context(self, queryset=None):
    return Profile.objects.select_related(user = self.request.user)

class ProfileUpdateView(UpdateView):
  model = Profile
  template_name = "profiles/update.html"
  form_class = forms.ProfileUpdateForm

  def get_success_url(self):
    return resolve_url('profiles:myprof', pk=self.kwargs['pk'])

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["process_name"] = "Update"
    return context