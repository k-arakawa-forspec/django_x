from django.urls import path
from .views import ProfileDetailView, MyProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('<int:user_id>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('my/', MyProfileDetailView.as_view(), name='my-profile'),
    path('my/update/', ProfileUpdateView.as_view(), name='profile-update'),
]
