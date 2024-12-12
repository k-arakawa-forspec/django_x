from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<slug:login_id>/", views.DetailView.as_view(), name="detail"),
    path("<slug:login_id>/follows/", views.FollowListView.as_view(), name="follow_list"),
    path("<slug:login_id>/followers/", views.FollowerListView.as_view(), name="follower_list")
]
