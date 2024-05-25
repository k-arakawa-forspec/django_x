from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kargs):
    super().__init__(*args, **kargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"
