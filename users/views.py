from django.views.generic.detail import DetailView as GenericDetailView
from accounts.models import User

# Create your views here.
class DetailView(GenericDetailView):
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

    context['follows_count'] = user.follow_user_set.count()
    context['followers_count'] = user.follower_user_set.count()
    
    return context

class FollowsView(GenericDetailView):
  model = User
  template_name = "users/follows.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # URL中の login_id に紐づくUserインスタンス
    # (Detailviewの実装によって既に取得されている)
    user = self.object

    # TODO 登録降順(follows.id desc)でソートしたいところだが
    # ManyToManyField で through を使用しておらず中間Modelがないことが影響してか
    # 対処のしようがない？
    follow_user_set = user.follow_user_set.select_related("profile").all()
    context['follow_user_set'] = follow_user_set

    return context

class FollowersView(GenericDetailView):
  model = User
  template_name = "users/followers.html"
  slug_url_kwarg = "login_id"
  slug_field = "login_id"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # URL中の login_id に紐づくUserインスタンス
    # (Detailviewの実装によって既に取得されている)
    user = self.object

    # TODO 登録降順(follows.id desc)でソートしたいところだが
    # ManyToManyField で through を使用しておらず中間Modelがないことが影響してか
    # 対処のしようがない？
    follower_user_set = user.follower_user_set.select_related("profile").all()
    context['follower_user_set'] = follower_user_set

    return context
