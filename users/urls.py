from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:login_id>/", views.HomeView.as_view(), name="home"),
]
