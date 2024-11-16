from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow_user_set',
            field=models.ManyToManyField(db_table='follows', related_name='follower_set_users', to=settings.AUTH_USER_MODEL),
        ),
    ]