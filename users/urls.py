from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:login_id>/", views.UserView.as_view(), name="user"),
]
