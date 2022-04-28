# Generated by Django 4.0.4 on 2022-04-27 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('enable', 'enable'), ('disable', 'disable')], default='disable', max_length=20, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coin', models.CharField(max_length=50, unique=True, verbose_name='Coin Name')),
                ('symbol', models.CharField(max_length=50, unique=True, verbose_name='Symbol Coin name')),
                ('lowprice', models.FloatField()),
                ('highprice', models.FloatField()),
                ('cointype', models.CharField(choices=[('notset', 'notset'), ('crypto', 'crypto'), ('fiat-irt', 'fiat-irt')], default='notset', max_length=50, verbose_name='Coin Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.FloatField(default=0, verbose_name='Balance')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='Update Time')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='uwallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coin_pairs', models.CharField(max_length=50, verbose_name='Coin pairs')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('paid', 'paid'), ('faild', 'faild'), ('expired', 'expired')], default='disable', max_length=20, verbose_name='وضعیت')),
                ('coin_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcoinin', to='coins.userwallet')),
                ('coin_out', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcoinout', to='coins.userwallet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
