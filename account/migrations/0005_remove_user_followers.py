# Generated by Django 4.2.7 on 2023-12-15 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_bio_user_followers_user_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
    ]
