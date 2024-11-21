from django.views.generic.detail import DetailView
from accounts.models import User

# Create your views here.
class BaseUserView(DetailView):
  model = User
  slug_url_kwarg = "login_id"
  slug_field = "login_id"


class DetailView(BaseUserView):
  template_name = "users/detail.html"

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

    # フォロー数
    context['follow_count'] = user.follow_user_set.all().count()

    # フォロワー数
    context['follower_count'] = user.follower_user_set.all().count()

    return context


class FollowsView(BaseUserView):
  template_name = "users/follows.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['follows'] = self.object.follow_user_set.all().select_related('profile')
    return context


class FollowersView(BaseUserView):
  template_name = "users/followers.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['followers'] = self.object.follower_user_set.all().select_related('profile')
    return context
