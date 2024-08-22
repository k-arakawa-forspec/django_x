from django.views.generic import DetailView
from .models import Profile


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    is_my_profile = False

    def get_queryset(self):
        return super().get_queryset().select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_my_profile'] = self.is_my_profile
        return context


class MyProfileView(ProfileView):
    is_my_profile = True

    def get_queryset(self):
        self.kwargs.update(pk=self.request.user.pk)
        return super().get_queryset()
