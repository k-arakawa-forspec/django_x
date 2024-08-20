from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
  path("<int:pk>", views.ProfileView.as_view(), name="profile"),
  path("my", views.MyProfileView.as_view(), name="profile"),
  path("my/update", views.UpdateProfileView.as_view(), name="update_profile")
]