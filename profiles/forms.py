from django import forms
from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):

  class Meta:
    model = Profile
    fields = ('self_introduction', )
    widgets = {
      'self_introduction': forms.Textarea(),
    }

class UsersHomeForm(ModelForm):

  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    for login_users_post_list in self.fields.values():
      login_users_post_list.widget.attrs["class"] = "UsersHomeInform"


