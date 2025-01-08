from django.urls.base import reverse
from django.views.generic import DetailView, UpdateView
from . import forms
from .models import Profile

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
    form_class = forms.ProfileForm
    template_name = "profiles/update_login_user.html"

    """
    URL上に `pk` パラメータを設けられないため
    get_object() をオーバーライドして直接取得
    """
    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_success_url(self):
        return reverse('profiles:detail_login_user')
