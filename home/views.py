from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
# 2025/02課題
from django.views.generic import TemplateView, ListView
from posts.models import Post

# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"

  # 2025/02課題
  # posts/viewsから丸コピ
  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
    #  post_list = Post.objects.all()
    # 最新が一番上にするからポストの新しい順に並び変える
     post_list = Post.objects.all().order_by('-created_at')
     context["post_list"] = post_list
     return context

  # URLリンクのメモ
  # /users/Kira_Yamato/
  # /users/Lacus_Clyne/follows/ 

  # posts/viewsからベースを丸コピ
  # これを下記条件に書き換える
  
  # 『ログインユーザがフォローしているユーザのポストを投稿降順（＝最新が上）で一覧表示する。』
  class ListView(ListView):
    template_name = "posts/list.html"
    model = Post
    def get_queryset(self):
      queryset = super().get_queryset()
      # ログインユーザの post の降順
      queryset = queryset.filter(user=self.request.user).order_by("id").reverse()
      return queryset