from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import SettingsForm

class SettingsView(FormView):
    template_name = 'settings/settings.html'
    form_class = SettingsForm

    def form_valid(self, form):
        # フォームが有効なら、選択されたカラーモードをクッキーに保存
        color_mode = form.cleaned_data['colorMode']
        response = super().form_valid(form)
        response.set_cookie('color_mode', color_mode)  # クッキーに保存
        return response

    def get_success_url(self):
        return reverse('settings:settings') # 設定画面