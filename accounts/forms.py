from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"


class SignUpForm(UserCreationForm):

  class Meta:
    model = User
    fields = (
        "login_id",
        "nickname",
    )
