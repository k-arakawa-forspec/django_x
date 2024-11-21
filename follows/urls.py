from django.urls import path
from . import views

app_name = "follows"

urlpatterns = [
    path("add/<int:user>/", views.FollowView.add, name="add"),
    path("remove/<int:user>/", views.FollowView.remove, name="remove"),
]
