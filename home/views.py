from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from posts.models import Post

# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # フォローユーザのポスト, 投稿降順
    # SELECT posts.id, ... users.id, ..., profiles.id
    #   <= N+1問題回避のため select_related() で user, profile も取得
    # FROM posts INNER JOIN users ... INNER JOIN follows ... LEFT OUTER JOIN profiles ...
    #   <= filter() で指定した post -> user -> follow_user_set(follows 経由の user) がINNER JOINされている
    #   <= profiles は select_related() しているだけのため外部結合(LEFT OUTER JOIN)にしてくれている模様
    # WHERE follows.from_user_id = [ログインユーザのid]
    # ORDER BY posts.created_at DESC
    post_list = Post.objects\
      .filter(user__follower_user_set__pk=self.request.user.pk)\
      .select_related("user__profile")\
      .order_by("-created_at")

    context['post_list'] = post_list

    return context
