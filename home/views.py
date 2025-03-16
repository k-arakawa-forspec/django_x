from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from posts.models import Post

# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.all().order_by('-created_at')
    context["post_list"] = post_list
    return context

class ListView(ListView):
  template_name = "posts/list.html"
  model = Post

  def get_queryset(self):
    user = self.request.user
    # ログインユーザーがフォローしているユーザーのIDを取得
    followed_users = user.follow_user_set.all()

    # フォローしているユーザーのポストを降順で取得
    queryset = Post.objects.filter(user__in=followed_users).order_by('-created_at')

    return queryset
