 # 2024/07/18 課題
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
  path('<int:pk>/', views.OtherProfView.as_view(), name='Otherprof'),
  path('my/', views.MyProfView.as_view(), name="myprof"),
  path('my/update', views.ProfileUpdateView.as_view(), name="update"),
]
