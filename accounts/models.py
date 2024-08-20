from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  # AbstractUser から継承される username を削除
  username = None

  login_id = models.CharField(max_length=20, unique=True)

  nickname = models.CharField(max_length=100)

  USERNAME_FIELD = 'login_id'
  REQUIRED_FIELDS = ['nickname']

  def save(self, *args, **kwargs):
    super().save(args, kwargs)
    Profile.objects.get_or_create(user=self)