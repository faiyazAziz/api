# Generated by Django 4.2.7 on 2023-12-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.ImageField(default='images/shirt.jpg', upload_to='images/'),
        ),
    ]