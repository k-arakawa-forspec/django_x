from django import forms
from django.forms import ModelForm
from .models import Profile

class UpdateProfileForm(ModelForm):

    class Meta:
      model = Profile
      fields = ('self_introduction', )
      widgets = {
        'self_introduction': forms.Textarea(attrs={'rows': 5}),
      }