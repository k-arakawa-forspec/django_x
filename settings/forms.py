from django import forms

COLOR_MODE_CHOICES = [
    ('light', 'ライトモード'),
    ('dark', 'ダークモード'),
]

class SettingsForm(forms.Form):
    colorMode = forms.ChoiceField(choices=COLOR_MODE_CHOICES, label='カラーモード')