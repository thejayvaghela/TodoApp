# Generated by Django 3.0.1 on 2020-04-11 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jayapp', '0003_user_cpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassword',
        ),
    ]