from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  login_id = models.CharField(max_length=20, unique=True)

  nickname = models.CharField(max_length=20)

  REQUIRED_FIELDS = ['login_id', 'nickname']
