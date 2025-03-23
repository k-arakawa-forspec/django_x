from django.views.generic import ListView
from posts.models import Post


# Create your views here.
class IndexView(ListView):
  template_name = "home/index.html"
  model = Post

  def get_queryset(self):
    return (
      super().get_queryset()
      .select_related('user__profile')
      .filter(user__follower_user_set=self.request.user)
      .order_by('-created_at')
    )
