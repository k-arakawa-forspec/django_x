from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)

    def get_following_users(self):
        """ フォローしているユーザーの一覧を取得 """
        return User.objects.filter(followers__follower=self)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # 投稿を降順に
