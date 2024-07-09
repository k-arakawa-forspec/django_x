from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.CreateView.as_view(), name="create"),

    # 24/6/20課題により追加
    # 自分のポストのみ表示
    path("mylist/", views.MyPostView.as_view(), name="mylist"),
]