from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<slug:login_id>/", views.ProifileDetail.as_view(), name="detail"),
    path("<slug:login_id>/follows",views.FollowingView.as_view(), name="following"),
    path("<slug:login_id>/followers",views.FollowersView.as_view(), name="followers"),
]
