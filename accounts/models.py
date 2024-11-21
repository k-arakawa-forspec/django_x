from django.db import models
from django.contrib.auth.models import AbstractUser
from profiles.models import Profile

class User(AbstractUser):
  class Meta:
    db_table = 'users'

  # AbstractUser から継承される username を削除
  username = None

  login_id = models.CharField(max_length=20, unique=True)

  nickname = models.CharField(max_length=100)

  USERNAME_FIELD = 'login_id'
  REQUIRED_FIELDS = ['nickname']

  follow_users = models.ManyToManyField(
    'self',
    db_table='follows',
    symmetrical=False,
    related_name='follower_users'
  )

  def save(self, *args, **kwargs):
    # https://docs.djangoproject.com/ja/5.0/ref/models/instances/#state
    adding = self._state.adding
    # 下記の実装でも同様
    #adding = not self._state.db
    #adding = self.pk is None

    super().save(args, kwargs)

    # save() でINSERTされる場合であっても
    # save() 後に `_state.adding` を参照すると False になる
    #print(f'adding after save: {self._state.adding}')

    # INSERTされる場合のみ Profile も create する
    if adding:
      Profile.objects.create(user=self)
      
   def is_following(self, follow_user_id):
    return self.follow_users.all().filter(id=follow_user_id).exists()
    