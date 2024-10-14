from django.views.generic import DetailView
from accounts.models import User
from posts.models import Post


# Create your views here.
class HomeView(DetailView):
  template_name = "users/home.html"
  model = User
  slug_field = "login_id"
  slug_url_kwarg = "login_id"

  def get_queryset(self):
    queryset = super().get_queryset()
    return User.objects.filter(login_id=self)



class PostView(DetailView):
  template_name = "posts/partials/post.html"
  model = Post

  def get_queryset(self):
    queryset = super().get_queryset()
    # login_idに紐づくのpostの降順
    queryset = queryset.filter(user=self.request.user).order_by("id").reverse()
    return queryset
