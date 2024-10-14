from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Profile, Post

# Create your views here.

class UserHomeView(DetailView):
    model = User
    template_name = 'user_profile.html'
    slug_field = 'login_id'
    slug_url_kwarg = 'login_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        profile = get_object_or_404(Profile, user=user)
        posts = Post.objects.filter(user=user).order_by('-created_at')
        context['profile'] = profile
        context['posts'] = posts
        context['form'] = ProfileForm(instance=profile)
        return context