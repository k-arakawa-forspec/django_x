from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("add/<int:user_id>/", views.AddView.as_view(), name="add"),
    path("remove/<int:user_id>/", views.RemoveView.as_view(), name="remove"),
]
