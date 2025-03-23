from django.views.generic import TemplateView
from posts.models import Post


# Create your views here.
class IndexView(TemplateView):
  template_name = "home/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # ログインユーザーがフォローしているユーザーIDのリストを取得する。
    ids = [followed_users.id for followed_users in self.request.user.follow_user_set.all()]
    post_list = Post.objects.filter(user__in=ids).order_by('-created_at')
    context['post_list'] = post_list

    return context
