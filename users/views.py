from django.views.generic.detail import DetailView
from accounts.models import User

# Create your views here.
class DetailView(DetailView):
  model = User
  template_name = "users/detail.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"
  UNIT_LIST = [ # 表示数値の単位変換用：昇順
      { "num": 1E3, "unit": "K" },
      { "num": 1E6, "unit": "M" },
      { "num": 1E9, "unit": "B" },
      { "num": 1E12, "unit": "T"}
    ]

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

    # フォロー数取得
    context['follow_count'] = self.unit_format(user.follow_user_set.all().count())

    # フォロワー数取得
    context['follower_count'] = self.unit_format(user.follower_user_set.all().count())

    return context

  def unit_format(self, count):
    if count < self.UNIT_LIST[0]["num"]:
      return count

    # 1000以上は単位変換
    for unit in reversed(self.UNIT_LIST):
      if count >= unit["num"]:
        return f'{count/unit["num"]:.1f}{unit["unit"]}'

class FollowsView(DetailView):
  template_name = "users/follows.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['follows_profile'] = self.object.follow_user_set.all().select_related('profile')
    return context

class FollowersView(DetailView):
  template_name = "users/followers.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['followers_profile'] = self.object.follower_user_set.all().select_related('profile')
    return context
