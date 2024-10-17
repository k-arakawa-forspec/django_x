from django.views.generic import DetailView
from accounts.models import User

class DashBoardView(DetailView):
  template_name = "users/dashboard.html"

  def get_object(self):
    user = User.objects.get(login_id=self.kwargs['login_id'])
    return user

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.object
    context['post_list'] = user.post_set.all().order_by('-id')
    return context
