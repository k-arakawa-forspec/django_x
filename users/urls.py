from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('users/<str:login_id>/', views.user_profile, name='user_profile'),
    path("<slug:login_id>/", views.DetailView.as_view(), name="detail"),
    path('users/<str:login_id>/followers/', views.follower_list, name='follower_list'),
]
