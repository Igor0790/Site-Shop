# Generated by Django 4.1.7 on 2023-03-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(default=None, upload_to='goods/categories/')),
                ('alt', models.CharField(default=None, max_length=100, verbose_name='ALT SRC')),
            ],
            options={
                'verbose_name': 'Media of Category',
                'verbose_name_plural': 'Media of Categories',
            },
        ),
    ]
