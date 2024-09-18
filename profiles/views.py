from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
    queryset = Profile.objects.select_related('user')

    def get_object(self, queryset=None):
        return Profile.objects.get(user_id=self.kwargs['user_id'])

class MyProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(user_id=self.request.user.id)

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profileUpdate.html'

    def get_success_url(self):
        return reverse_lazy('myProfile')
