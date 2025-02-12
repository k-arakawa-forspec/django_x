from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SettingForm


# Create your views here.
class IndexView(FormView):
  form_class = SettingForm
  template_name = "settings/index.html"
  success_url = reverse_lazy('settings:index')

  def get_initial(self):
    # SettingForm の初期値設定
    initial = super().get_initial()
    initial["color_mode_dark"] = self.request.COOKIES.get("color_mode") == "dark"

    return initial

  def form_valid(self, form):
    response = super().form_valid(form)
    color_mode_dark = form.cleaned_data["color_mode_dark"]

    if color_mode_dark:
      max_age = 60 * 60 * 24 * 365
      response.set_cookie("color_mode", value="dark", max_age=max_age)
    else:
      response.delete_cookie("color_mode")

    return response
