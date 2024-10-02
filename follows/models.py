from django.db import models

# Create your models here.
class Follow(models.Model):
  class Meta:
    db_table = 'follows'

  # User モデルからは follow_set で参照することになる
  user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  # related_name を指定しない場合 User モデルからはこちらも follow_set で参照することになってしまい
  # follow_set で名前解決できなくなることになってしまうため
  # そもそも related_name を指定しないと makemigrations でエラーとなる
  follow_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='follower')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.pk)
