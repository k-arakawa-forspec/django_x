from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<slug:login_id>/", views.DetailView.as_view(), name="detail"),
    path("<slug:login_id>/followList", views.FollowListView.as_view(), name="followList"),
    path("<slug:login_id>/followerList", views.FollowerListView.as_view(), name="followerList"),
]
