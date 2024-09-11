from django.apps import AppConfig
from django.db.models import BigAutoField

class ProfilesConfig(AppConfig):
    default_auto_field = BigAutoField
    
    name = 'profiles'
