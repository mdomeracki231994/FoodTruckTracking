# Generated by Django 5.0.1 on 2024-01-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_appuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
