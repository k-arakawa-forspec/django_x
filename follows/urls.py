from django.urls import path
from . import views

app_name = 'follows'

urlpatterns = [
    path('<str:action>/<int:pk>/', views.FollowToggleView.as_view(), name="toggle"),
]