from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView
from accounts.models import User

# Create your views here.

class FollowView(DetailView):
    model = User
    pk_url_kwarg = "user"
    pk_field = "user"

    def add_follow(request, user):
        follow_user = User.objects.get(id=user)
        request.user.follow_user_set.add(follow_user.pk)
        return redirect('users:detail', login_id=follow_user.login_id)

    def remove_follow(request, user):
        follow_user = User.objects.get(id=user)
        request.user.follow_user_set.remove(follow_user.pk)
        return redirect('users:detail', login_id=follow_user.login_id)