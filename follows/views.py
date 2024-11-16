from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView
from accounts.models import User
# Create your views here.
class FollowView(DetailView):
    model = User
    pk_url_kwarg = "user"
    pk_field = "user"

    def add(request, user):
        user = User.objects.get(id=user)
        request.user.follow_users.add(user.pk)
        return redirect('users:detail', login_id=user.login_id)

    def remove(request, user):
        user = User.objects.get(id=user)
        request.user.follow_users.remove(user.pk)
        return redirect('users:detail', login_id=user.login_id)