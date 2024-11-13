from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from accounts.models import User

class FollowToggleView(RedirectView):
    def post(self, *args, **kwargs):
        action = kwargs.get('action')
        user = get_object_or_404(User, pk=kwargs.get('pk'))

        # トグルアクションでフォロー/フォロー解除
        if action == 'add':
            self.request.user.follow_user_set.add(user)
        elif action == 'remove':
            self.request.user.follow_user_set.remove(user)
        
        return HttpResponseRedirect(reverse('users:detail', kwargs={'login_id': user.login_id}))