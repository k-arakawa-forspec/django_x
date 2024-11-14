from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from posts.models import Post

class FollowFollowerView(DetailView):
    pattern_name = 'users:detail'
    model = User
    pk_url_kwarg = "login_id"

 
    # フォロー機能
    def follow_view(request, *args, **kwargs):
        return 

    # フォロー解除
    def unfollow_view(request, *args, **kwargs):
        return 