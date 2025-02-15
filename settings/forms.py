from django import forms

class SettingForm(forms.Form):
    is_dark_mode = forms.BooleanField(
        required=False, 
        label="ダークモードON", 
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
