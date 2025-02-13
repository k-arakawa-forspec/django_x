from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("appearance/", views.AppearanceView.as_view(), name="appearance"),
]
