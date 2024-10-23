from django import forms

class SettingForm(forms.Form):
  color_mode_dark = forms.BooleanField(label="ダークモード表示", label_suffix="", required=False)
