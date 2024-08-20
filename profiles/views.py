from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from . import forms
from .models import Profile


class ProfileView(DetailView):
  template_name = 'profiles/profile.html'
  model = Profile
  queryset = Profile.objects.select_related('user')

class MyProfileView(DetailView):
  template_name = 'profiles/profile.html'
  model = Profile
  
  def get_object(self, queryset=None):
    return Profile.objects.get(user_id=self.request.user.id)

class UpdateProfileView(UpdateView):
  form_class = forms.UpdateProfileForm
  template_name = 'profiles/update_profile.html'
  model = Profile
  success_url = reverse_lazy("profiles:profile")
  
  def get_object(self, queryset=None):
    return Profile.objects.get(user_id=self.request.user.id)
