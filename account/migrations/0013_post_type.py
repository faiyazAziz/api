# Generated by Django 4.2.6 on 2024-02-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_post_media_remove_user_profilepic_post_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='image', max_length=250),
        ),
    ]