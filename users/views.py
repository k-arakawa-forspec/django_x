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
    # ログイン中のUserインスタンス
    logged_in_user = self.request.user
    context['post_list'] = post_list
    context['is_followed'] = logged_in_user.follow_user_set.filter(id=user.id).count() == 1
    context['is_me'] = logged_in_user == user
    return context
