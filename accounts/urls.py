from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),

    # 24/6/20課題により追加
    path("mylist/", views.MyListView.as_view(), name="mylist"),
]
