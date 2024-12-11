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

    user = get_object_or_404(User, username=login_id)
    follow_count = user.following.count()
    follower_count = user.followers.count()

    return context

  def follower_list(request, login_id):
    user = get_object_or_404(User, username=login_id)
    followers = user.followers.all()
    return render(request, 'users/follower_list.html', {
        'user': user,
        'followers': followers,
    })

  def follow_list(request, login_id):
    user = get_object_or_404(User, username=login_id)
    follows = user.following.all()
    return render(request, 'users/follow_list.html', {
        'user': user,
        'follows': follows,
    })
