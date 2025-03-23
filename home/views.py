from django.views.generic import ListView
from posts.models import Post


# Create your views here.
class IndexView(ListView):
  template_name = "home/index.html"
  model = Post
  ordering = ['-created_at']

  def get_queryset(self):
    queryset = super().get_queryset()
    ids = [followed_users.id for followed_users in self.request.user.follow_user_set.all()]
    queryset = queryset.filter(user__in=ids)
    return queryset
