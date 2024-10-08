from django.views.generic import DetailView
from profiles.models import Profile

from posts.models import Post
from profiles import forms
# from users import forms


class UsersHomeView(DetailView):
  form_class = forms.UsersHomeForm
  template_name = "users/usershome.html"
  model = Profile

  # 投稿情報取得
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    login_users_post_list = Post.objects.filter(user=self.request.user)
    context["login_users_post_list"] = login_users_post_list
    return context
  

# class LoginUsersPostIndex(DetailView):
#   template_name = "posts/partials/post.html"
#   model = Post

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     post_list = Post.objects.filter(user=self.request.user)
#     context["post_list"] = post_list
#     return context