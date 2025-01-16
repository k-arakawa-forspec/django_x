from django.views.generic import TemplateView, FormView
from settings.form import AppearanceForm


class IndexView(TemplateView):
  template_name = 'settings/index.html'


class AppearanceView(FormView):
    template_name = 'settings/appearance.html'
    form_class = AppearanceForm
    success_url = '/settings/appearance'

    def form_valid(self, form):
        return super().form_valid(form)
