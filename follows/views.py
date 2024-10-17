from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from accounts.models import User


# Create your views here.
class BaseView(RedirectView):
    pattern_name = 'users:detail'
    logged_in_user = None
    user = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.logged_in_user = request.user
        self.user = get_object_or_404(User, pk=kwargs['pk'])


class AddView(BaseView):

    def get_redirect_url(self, *args, **kwargs):
        self.logged_in_user.follow_user_set.add(self.user)
        return super().get_redirect_url(login_id=self.user.login_id)


class RemoveView(BaseView):

    def get_redirect_url(self, *args, **kwargs):
        self.logged_in_user.follow_user_set.remove(self.user)
        return super().get_redirect_url(login_id=self.user.login_id)
