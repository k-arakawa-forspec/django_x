from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    self_introduction = models.TextField()
class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    self_introduction = models.TextField()
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)
    class Meta:
        ordering = ['-created_at']