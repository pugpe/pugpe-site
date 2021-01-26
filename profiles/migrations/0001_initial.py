# Generated by Django 3.1.5 on 2021-01-26 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='users.user', verbose_name='user')),
                ('full_name', models.CharField(max_length=128, verbose_name='full name')),
                ('about_me', models.TextField(blank=True, verbose_name='about me')),
                ('telegram_user', models.CharField(blank=True, max_length=64, verbose_name='telegram user')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]