from django.views.generic import DetailView
from accounts.models import User


# Create your views here.
class UserView(DetailView):
    template_name = 'users/user.html'


    def get_object(self):
        return User.objects.get(login_id=self.kwargs['login_id'])
