from django.db import models


# Create your models here.
class Post(models.Model):
  user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  content = models.CharField('投稿内容', max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.id
