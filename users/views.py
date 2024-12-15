from django.views.generic.detail import DetailView
from accounts.models import User

# Create your views here.
class DetailView(DetailView):
  model = User
  template_name = "users/detail.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # URL中の login_id に紐づくUserインスタンス
    # (Detailviewの実装によって既に取得されている)
    user = self.object

    # Userに紐づくPostのリスト
    post_list = user.post_set.all().order_by('-id')
    context['post_list'] = post_list

    # フォローしているか否か
    followed = self.request.user.follow_user_set.filter(id=user.id).exists()
    context['followed'] = followed

    # フォロー人数表示用のカウント
    context['follow_count'] = user.follow_user_set.count()

    # フォロワー人数表示用のカウント
    context['follower_count'] = user.follower_user_set.count()

    return context

class FollowListView(DetailView):
  model = User
  template_name = "users/followList.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"
  context_object_name = "user"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

class FollowerListView(DetailView):
  model = User
  template_name = "users/followerList.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"
  context_object_name = "user"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context