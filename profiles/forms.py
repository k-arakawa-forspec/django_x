from django.forms import ModelForm
from .models import Profile
class ArticleForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["self_introduction"]