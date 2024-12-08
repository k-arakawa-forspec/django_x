from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<slug:login_id>/", views.DetailView.as_view(), name="detail"),
    path("<slug:login_id>/follows/", views.FollowsView.as_view(), name="follows"),
    path("<slug:login_id>/followers/", views.FollowersView.as_view(), name="followers"),
]
