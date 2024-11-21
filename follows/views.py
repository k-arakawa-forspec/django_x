from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

class addView(RedirectView):
    pattern_name = "users:detail"

    # フォロー機能
    def follow_view(self, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs["user_id"]);
        follow_user = self.request.user
        request.follow_user_set.add(follow_user)
        return redirect('users:detail', login_id=follow_user.login_id)
        
class removeView(RedirectView):
    pattern_name = "users:detail"

    # フォロー解除
    def unfollow_view(self, *args, **kwargs):
        to_user = get_object_or_404(User, pk=kwargs["user_id"]);
        from_user = self.request.user
        request.follow_user_set.remove(follow_user)
        return redirect('users:detail', login_id=follow_user.login_id)
