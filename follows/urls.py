from django.urls import path
from . import views

app_name = "follows"

urlpatterns = [
    # フォロー
    path('add/<int:user>', views.FollowFollowerView.follow_view, name='add_follow'),
    # フォロー解除
    path('remove/<int:user>', views.FollowFollowerView.unfollow_view, name='remove_follow'),
]
