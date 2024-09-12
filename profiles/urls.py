from django.urls import path
from . import views

app_name = "plofiles"

urlpatterns = [
    path("<int:pk>/", views.DetailView.as_view(), name="plofile"),
    path("my/", views.MyDetailView.as_view(), name="my"),
    path("my/update/", views.UpdateView.as_view(), name="my_update"),
]
