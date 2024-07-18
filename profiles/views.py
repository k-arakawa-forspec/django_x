from django.views.generic import DetailView
from .models import Profile


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'

    def get_queryset(self):
        return super().get_queryset().select_related('user')
