from django import forms


class AppearanceForm(forms.Form):
    is_dark_theme = forms.BooleanField(required=False, initial=False)
