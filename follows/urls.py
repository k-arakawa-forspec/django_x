from django.urls import path
from . import views

app_name = "follows"

urlpatterns = [
    path("add/<int:user>/", views.FollowView.add_follow, name="add_follow"),
    path("remove/<int:user>/", views.FollowView.remove_follow, name="remove_follow"),
]