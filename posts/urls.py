from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.CreateView.as_view(), name="create"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("", views.ListView.as_view(), name="list"),
]
