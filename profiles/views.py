from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, UpdateView

from posts.views import IndexView
from .models import Profile

from . import forms



class MyDeteilView(DetailView):
  model = Profile
  template_name = 'profile/detail.html' 
  context_object_name = "profiles"

class DeteilView(DetailView):
  model = Profile
  template_name = 'profile/detail.html' 
  context_object_name = "profiles"

class UpdateView(UpdateView):
  model = Profile
  context_object_name = "profiles"
  template_name = 'profile/update.html' 
  fields = ("title", "memo", "priority", "deadline")
  def get_success_url(self):
      return reverse_lazy("profiles:detail", kwargs={'pk': self.object.pk})




