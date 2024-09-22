from django.views.generic import DetailView, UpdateView
from .models import Profile
from . import forms
from django.urls import reverse_lazy


# Create your views here.
class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    # `OneToOneField: User.id <=> Profile.user_id` であるため、明示的な `Profile => User` の取得は不要っぽい？
    # queryset = Profile.objects.select_related('user')


class MyProfileView(ProfileView):

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = forms.ProfileUpdateForm
    template_name = 'profiles/update.html'
    success_url = reverse_lazy('profiles:my')

    def get_queryset(self):
        # Error: "Generic detail view ProfileUpdateView must be called with either an object pk or a slug in the URLconf."
        # PK指定がないURL設定でエラーが発生するため、ログインユーザーのPKを設定することで解消。
        self.kwargs.update(pk=self.request.user.pk)
        return super().get_queryset()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
