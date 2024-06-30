from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.ListView.as_view(), name="list"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("index/", views.IndexView.as_view(), name="index"),
]
