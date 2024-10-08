from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/", views.UsersHomeView.as_view(), name="UsersHomeView"),
    # path("<int:pk>/test/" , views.LoginUsersPostIndex.as_view(), name="LoginUsersPostIndex"),
]
