from django.views.generic.detail import DetailView
from accounts.models import User

# Create your views here.
class ProifileDetail(DetailView):
  model = User
  template_name = "users/detail.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"

  def get_context_data(self, **kwargs):
    model = User
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

    #フォロー数/フォロワー数の取得
    context['following'] = user.follow_user_set.count()
    context['follower'] = user.follower_user_set.count()

    return context


class FollowingView(DetailView):
  template_name = "users/following.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['following'] = self.request.user.follow_user_set.all().select_related('profile')
    return context


class FollowersView(DetailView):
  template_name = "users/followers.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['follower'] = self.request.user.follower_user_set.all().select_related('profile')
    return context