from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

  class Meta:
    model = Post
    fields = ('content', )
    widgets = {
      'content': forms.Textarea(
        attrs={
          'rows': 10,
          'cols': 80,
          'class': 'form-control',
        }
      ),
    }
