from decimal import Decimal, ROUND_DOWN
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
    context['follow_count'] = self.format_count(user.follow_user_set.all().count())

    # フォロワー数
    context['follower_count'] = self.format_count(user.follower_user_set.all().count())

    return context


  """ Formatted sample.
  n = 9 => "9"
  n = 99 => "99"
  n = 999 => "0.9K"
  n = 1,000 => "1.0K"
  n = 9,999 => "9.9K"
  n = 99,999 => "99.9K"
  n = 999,999 => "999.9K"
  n = 1,000,000 => "1.0M"
  n = 9,999,999 => "9.9M"
  n = 99,999,999 => "99.9M"
  n = 999,999,999 => "999.9M"
  n = 1,000,000,000 => "1.0B"
  n = 9,999,999,999 => "9.9B"
  """
  def format_count(self, n):
    units = ['K', 'M', 'B']
    u = ''
    for unit in units:
      tmp = n / 1000
      if tmp < 0.1: break
      n = tmp
      u = unit
      if n / 1000 < 1: break

    n = str(Decimal(str(n)).quantize(Decimal('.1'), rounding=ROUND_DOWN)) if u != '' else str(n)
    return n + u


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
