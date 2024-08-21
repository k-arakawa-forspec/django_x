 # 2024/07/18 課題
from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
  path('prof/', views.OtherProfView.as_view(), name='Otherprof'),
  path("<int:pk>/my/", views.MyProfView.as_view(), name="myprof"),
  path("<int:pk>/my/update", views.ProfileUpdateView.as_view(), name="update"),
]
