# Generated by Django 3.1.7 on 2021-06-13 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_extension', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_management.user'),
        ),
    ]