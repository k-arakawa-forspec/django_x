from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"
