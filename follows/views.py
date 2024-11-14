from django.shortcuts import redirect
from django.urls.base import reverse
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from posts.models import Post

class FollowFollowerView(DetailView):
    pattern_name = 'users:detail'
<<<<<<< HEAD
    model = User
    pk_url_kwarg = "login_id"

 
    # フォロー機能
    def follow_view(request, *args, **kwargs):
        return 

    # フォロー解除
    def unfollow_view(request, *args, **kwargs):
        return 
=======
    pk_url_kwarg = "user"

    # フォロー機能
    def follow_view(request, user):
        follow_user = User.objects.get(id=user)
        request.user.follow_user_set.add(follow_user.pk)
        return redirect('users:detail', login_id=follow_user.login_id)

    # フォロー解除
    def unfollow_view(request, user):
        follow_user = User.objects.get(id=user)
        request.user.follow_user_set.remove(follow_user.pk)
        return redirect('users:detail', login_id=follow_user.login_id)
>>>>>>> cbdaedf (一部修正分)
