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

    # フォロー数のカウント
    context['follow_count'] = user.follow_user_set.count()

    # フォロワー数のカウント
    context['follower_count'] = user.follower_user_set.count()

    return context

class FollowListView(ListView):
  model = User
  template_name = "users/follow_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    login_id = self.kwargs.get('login_id')
    user = User.objects.get(login_id=login_id)

    context['profile_user'] = user
    context['follows'] = user.follow_user_set.select_related('profile')
    return context

class FollowerListView(ListView):
  model = User
  template_name = "users/follower_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    login_id = self.kwargs.get('login_id')
    user = User.objects.get(login_id=login_id)
    
    context['profile_user'] = user
    context['follower'] = user.follower_user_set.select_related('profile')
    return context
