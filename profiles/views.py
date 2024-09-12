from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Profile
from django.views.generic.edit import UpdateView
from . import forms
class ProfileView(DetailView):
  model = Profile
  context_object_name = "profile"
  
class MyProfileView(DetailView):
  
  model = Profile
  context_object_name = "profile"
  def get_object(self, queryset=None):
    return Profile.objects.filter(user_id = self.request.user.id).first()

class UpdateProfileView(UpdateView):
  model = Profile
  form_class = forms.ProfileForm
  template_name = "profiles/profile_update.html"
  success_url = reverse_lazy("profiles:my_profile")
  context_object_name = "profile"
  def get_object(self, queryset=None):
    return Profile.objects.filter(user_id = self.request.user.id).first()
  
