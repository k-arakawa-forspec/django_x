from django.shortcuts import render
from django.views.generic import DetailView
from posts.models import Post
from profiles.models import Profile
from accounts.models import User

# Create your views here.

class UserDetailView(DetailView):
  template_name = "users/user_detail.html"
  model = User
  slug_field = 'login_id'
  slug_url_kwarg = 'login_id'
  
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    post_list = Post.objects.filter(user=User.objects.get(login_id=self.kwargs['login_id'])).order_by("-created_at")
    context["post_list"] = post_list

    profile = Profile.objects.get(user=User.objects.get(login_id=self.kwargs['login_id']))
    context["profile"] = profile
    
    return context
  
  