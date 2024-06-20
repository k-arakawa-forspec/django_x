from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from . import forms
from .models import Post


# Create your views here.
class ListView(ListView):
  template_name = "posts/list.html"
  model = Post
  ordering = ["-id"]

  def get_queryset(self):
    return super().get_queryset().filter(user_id=self.request.user.id)


class CreateView(CreateView):
  form_class = forms.PostForm
  template_name = "posts/create.html"
  success_url = reverse_lazy("accounts:home")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class IndexView(TemplateView):
  template_name = "posts/list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.all()
    context["post_list"] = post_list
    return context
