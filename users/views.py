from django.views.generic.detail import DetailView
from accounts.models import User

# Create your views here.
class PostsView(DetailView):
  model = User
  template_name = "users/posts.html"
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
    return context
