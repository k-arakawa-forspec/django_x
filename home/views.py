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
      .filter(user_id__in=[user.id for user in self.request.user.follow_user_set.all()])
      .order_by('-created_at')
    )
