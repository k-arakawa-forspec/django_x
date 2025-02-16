from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SettingForm

class SettingView(FormView):
    template_name = 'settings/settings.html'
    form_class = SettingForm
    success_url = reverse_lazy('settings:settings')
    
    # トグルの初期状態を設定
    def get_initial(self):
        initial = super().get_initial()
        color_mode = self.request.COOKIES.get('color_mode', 'light')
        if color_mode == 'dark':
            initial['is_dark_mode'] = True
        else:
            initial['is_dark_mode'] = False
        return initial

    def form_valid(self, form):
        color_mode = 'dark' if form.cleaned_data['is_dark_mode'] else 'light'
        response = super().form_valid(form)
        response.set_cookie('color_mode', color_mode)
        return response