from django.views.generic import DetailView

from accounts.models import User
from posts.models import Post
from profiles.models import Profile


class DashBoardView(DetailView):
  template_name = "users/dashboard.html"

  def get_object(self):
    user = User.objects.get(login_id=self.kwargs['login_id'])
    if user != self.request.user:
      raise Exception("403エラー")
    return user

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['post_list'] = Post.objects.filter(user=self.request.user).order_by('-created_at')
    context['profile'] = Profile.objects.get(user=self.request.user)
    return context
