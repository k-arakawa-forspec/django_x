from django.views.generic import DetailView
from accounts.models import User
from posts.models import Post


# Create your views here.
class UserView(DetailView):
    template_name = 'users/user.html'
    user = None

    def set_user(self):
        self.user = User.objects.get(login_id=self.kwargs['login_id'])

    def get_object(self):
        self.set_user()
        return self.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.user.posts.all().order_by('-id')
        return context
