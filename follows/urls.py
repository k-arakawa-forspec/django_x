from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:user>/', views.add_follow, name='add_follow'),
    path('remove/<int:user>/', views.remove_follow, name='remove_follow'),
]
