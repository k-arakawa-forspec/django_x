from django.urls.base import reverse
from django.views.generic import DetailView, UpdateView
from .models import Profile

# Create your views here.
class DetailView(DetailView):
  template_name = "profiles/detail.html"
  model = Profile

class DetailLoginUserView(DetailView):
  template_name = "profiles/detail.html"

  """
  URL上に `pk` パラメータを設けられないため
  get_object() をオーバーライドして直接取得
  """
  def get_object(self):
    return Profile.objects.get(user=self.request.user)

class UpdateLoginUserView(UpdateView):
  template_name = "profiles/update_login_user.html"
  fields = ["self_introduction"]

  """
  URL上に `pk` パラメータを設けられないため
  get_object() をオーバーライドして直接取得
  """
  def get_object(self):
    return Profile.objects.get(user=self.request.user)

  def get_success_url(self):
    return reverse('profiles:detail_login_user')
