from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):

  class Meta:
    model = Profile
    fields = ('image', 'self_introduction',)
    #profile_picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    widgets = {
      'image':forms.ClearableFileInput(),
      'self_introduction': forms.Textarea(),
    }


