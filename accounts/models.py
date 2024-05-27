from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  # AbstractUser から継承される username を削除
  username = None

  login_id = models.CharField(max_length=20, unique=True)

  nickname = models.CharField(max_length=100)

  USERNAME_FIELD = 'login_id'
  REQUIRED_FIELDS = ['nickname']
