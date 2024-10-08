from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<slug:login_id>/", views.PostsView.as_view(), name="posts"),
]
