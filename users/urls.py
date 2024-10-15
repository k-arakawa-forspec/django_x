from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:login_id>/", views.DashBoardView.as_view(), name="dashboard"),
]
