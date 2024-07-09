from django.contrib.auth import login
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from . import forms
from .models import Post

# 24/6/20課題により追加
from django.shortcuts import render
from django.views import View
from django.views.generic.base import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import posts


# Create your views here.
class CreateView(CreateView):
  form_class = forms.PostForm
  template_name = "posts/create.html"
  success_url = reverse_lazy("accounts:home")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

# 全ユーザポスト表示
class IndexView(TemplateView):
  template_name = "posts/list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.all()
    context["post_list"] = post_list
    return context

# 24/6/20課題により追加
# ------------------------------------------------------------------------
class MyPostView(LoginRequiredMixin , ListView):
  """自分の投稿のみ表示"""
  model = Post
  template_name = 'posts/mylist.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.filter(user=self.request.user)
    #.order_by('-id')
    context["post_list"] = post_list
    return context
# ------------------------------------------------------------------------