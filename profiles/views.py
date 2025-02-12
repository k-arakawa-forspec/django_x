from django.urls import reverse
from django.views.generic import DetailView, UpdateView, View
from django.http import HttpResponseRedirect
from . import forms
from .models import Profile

class DetailView(DetailView):
    template_name = "profiles/detail.html"
    model = Profile

class DetailLoginUserView(DetailView):
    template_name = "profiles/detail.html"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color_mode"] = self.request.COOKIES.get("color_mode", "light")  # デフォルトはライトモード
        return context

class UpdateLoginUserView(UpdateView):
    form_class = forms.ProfileForm
    template_name = "profiles/update_login_user.html"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_success_url(self):
        return reverse('profiles:detail_login_user')

class ColorModeUpdateView(View):
    """
    カラーモードを変更するビュー
    """
    def post(self, request, *args, **kwargs):
        current_mode = request.COOKIES.get("color_mode", "light")
        new_mode = "dark" if current_mode == "light" else "light"

        response = HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("profiles:detail_login_user")))
        response.set_cookie("color_mode", new_mode, max_age=365*24*60*60)  # 1年間保持
        return response
