from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<str:login_id>", views.UserDetailView.as_view(), name="user_detail")
]
