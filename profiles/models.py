from django.db import models
import os

def user_profile_image_path(instance, filename):
  basename, ext = os.path.splitext(filename)
  return 'users/{0}/profile{1}'.format(instance.user.id, ext)

# Create your models here.
class Profile(models.Model):
  class Meta:
    db_table = 'profiles'

  user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True)
  self_introduction = models.CharField('自己紹介', max_length=1024)
  image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.self_introduction;
