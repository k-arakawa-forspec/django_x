from django.urls import path
from . import views

app_name = "follows"

urlpatterns = [
    path("add/<int:pk>/", views.AddView.as_view(), name="add"),
    path("remove/<int:pk>/", views.RemoveView.as_view(), name="remove"),
]
