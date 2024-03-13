# Generated by Django 4.2.7 on 2024-02-01 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profilePic',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_url',
            field=models.CharField(default='default', max_length=600),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_url',
            field=models.CharField(default='default', max_length=600),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.post')),
            ],
        ),
    ]