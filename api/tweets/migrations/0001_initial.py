# Generated by Django 3.1.4 on 2021-01-17 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('twitter_id', models.TextField(unique=True)),
                ('favorite_count', models.IntegerField(null=True)),
                ('user_id', models.TextField()),
                ('user_name', models.TextField(null=True)),
                ('text', models.TextField()),
                ('truncated', models.BooleanField(default=False)),
                ('time', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('short_url', models.URLField()),
                ('resolved_url', models.URLField(null=True)),
                ('domain', models.TextField(null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.tweet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
