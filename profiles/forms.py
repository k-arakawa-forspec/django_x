from .models import Profile

class ProfileUpdateForm():
  class Meta:
    model = Profile
    fields = ('self_introduction')
  