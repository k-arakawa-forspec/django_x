from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Post

# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"

  def get_context_data(self, **kwargs):
    # フォローしているユーザーIDを一度に取得
    followed_user_ids = self.request.user.follow_user_set.values_list('id', flat=True)
    # フォローしているユーザーのポストと関連情報を降順で取得
    post_list = Post.objects.select_related('user__profile').filter(user__id__in=followed_user_ids).order_by('-created_at')

    context = super().get_context_data(**kwargs)
    context["post_list"] = post_list
    return context
