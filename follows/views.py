from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from accounts.models import User

# Create your views here.
class AddView(RedirectView):
    pattern_name = "users:detail"

    def get_redirect_url(self, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs["user_id"]);
        from_user = self.request.user
        from_user.follow_user_set.add(to_user)

        return super().get_redirect_url(login_id=to_user.login_id)

class RemoveView(RedirectView):
    pattern_name = "users:detail"

    def get_redirect_url(self, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs["user_id"]);
        from_user = self.request.user
        from_user.follow_user_set.remove(to_user)

        return super().get_redirect_url(login_id=to_user.login_id)
