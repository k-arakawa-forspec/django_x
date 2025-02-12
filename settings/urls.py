from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
    path("Invert/", views.InvertView.as_view(), name="invert"),
]
