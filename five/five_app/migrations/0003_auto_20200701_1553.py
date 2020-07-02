# Generated by Django 3.0.3 on 2020-07-01 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('five_app', '0002_auto_20200701_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
