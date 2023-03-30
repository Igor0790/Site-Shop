# Generated by Django 4.1.7 on 2023-03-20 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Full Name')),
                ('phone', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=50, null=True)),
                ('balance', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('avatar', models.ImageField(blank=True, default=None, null=True, upload_to='users/', verbose_name='Avatar')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usermodel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]