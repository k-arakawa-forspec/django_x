from django.views.generic import TemplateView, FormView
from settings.form import AppearanceForm


class IndexView(TemplateView):
  template_name = 'settings/index.html'


class AppearanceView(FormView):
    template_name = 'settings/appearance.html'
    form_class = AppearanceForm
    success_url = '/settings/appearance'

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('is_dark_theme', form.cleaned_data['is_dark_theme'])
        return response
