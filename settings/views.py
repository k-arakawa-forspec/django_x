from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SettingForm

class SettingView(FormView):
    template_name = 'settings/settings.html'
    form_class = SettingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        color_mode = self.request.COOKIES.get('color_mode', 'light')
        # トグルの初期状態
        if color_mode == 'dark':
            context['form'].fields['is_dark_mode'].initial = True
        else:
            context['form'].fields['is_dark_mode'].initial = False
        return context

    def form_valid(self, form):
        color_mode = 'dark' if form.cleaned_data['is_dark_mode'] else 'light'
        response = HttpResponseRedirect(reverse('settings:settings'))
        response.set_cookie('color_mode', color_mode)
        return response