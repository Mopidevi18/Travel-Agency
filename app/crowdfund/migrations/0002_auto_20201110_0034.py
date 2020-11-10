# Generated by Django 3.0.3 on 2020-11-09 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crowdfund', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundraiser',
            name='category',
        ),
        migrations.AddField(
            model_name='fundraiser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fundraiser', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
