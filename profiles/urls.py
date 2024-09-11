from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>', views.ProfView.as_view(), name='profile'),
    path('my', views.MyProfView.as_view(), name='my'),
    path('my/update', views.ProfileUpdateView.as_view(), name='update'),
]