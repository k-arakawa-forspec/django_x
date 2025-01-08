from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("my/", views.DetailLoginUserView.as_view(), name="detail_login_user"),
    path("my/update/", views.UpdateLoginUserView.as_view(), name="update_login_user"),
]