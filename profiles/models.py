from django.db import models

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True)
  name = models.CharField(max_length=100)
  birthday = models.DateField(null=True, blank=True)
  favorite = models.TextField(null=True, blank=True)
  comment = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.user.username