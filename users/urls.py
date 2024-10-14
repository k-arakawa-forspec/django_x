from django.urls import path
from .views import UserHomeView
urlpatterns = [
    path('users/<slug:login_id>/', UserHomeView.as_view(), name='user_profile'),
]