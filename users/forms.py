from django import forms
from django.forms import widgets,ModelForm

from accounts.models import User
from posts.models import Post
from profiles.models import Profile

class UsersHomeForm(ModelForm):
  class Meta:
    model = User, Post, Profile
    fields = ('User.nickname','User.login_id',)
    widget = {
      'nickname': forms.Textarea(),
      'login_id': forms.Textarea(),
    }

  # nickname = widgets.CharField(attrs={'class': 'nickname'})
  # login_id = widgets.CharField(attrs={'class': 'login_id'})

  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    for UsersHomeInform in self.fields.values():
      UsersHomeInform.widget.attrs["class"] = "UsersHomeInform"
