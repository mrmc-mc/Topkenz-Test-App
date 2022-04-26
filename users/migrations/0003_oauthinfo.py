# Generated by Django 4.0.4 on 2022-04-25 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_personalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OauthInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('secret', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Oauth secret')),
                ('uri', models.CharField(blank=True, max_length=2500, null=True, unique=True, verbose_name='Oauth uri')),
                ('is_enabled', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uauth', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]
