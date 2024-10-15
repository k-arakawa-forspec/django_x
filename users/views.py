from django.views.generic import DetailView
from accounts.models import User
from posts.models import Post


# Create your views here.
class HomeView(DetailView):
  template_name = "users/home.html"
  model = User
  slug_field = "login_id"
  slug_url_kwarg = "login_id"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.filter(user=self.request.user).order_by("id").reverse()
    context["post_list"] = post_list
    return context
