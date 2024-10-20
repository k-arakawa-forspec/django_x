import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('follows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
           name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_id', to=settings.AUTH_USER_MODEL)),
                ('to_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_id', to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]