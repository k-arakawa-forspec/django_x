from django.db import models

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True)
  self_introduction = models.CharField('自己紹介', max_length=1024)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.pk
