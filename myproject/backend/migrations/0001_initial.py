# Generated by Django 5.1.1 on 2025-02-19 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picture_url', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('admin_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('comment', models.CharField(max_length=255)),
                ('read', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('read', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'db_table': 'message',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('publisher_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField()),
                ('avatar', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Collect',
                'verbose_name_plural': 'Collects',
                'db_table': 'collect',
                'unique_together': {('from_id', 'post_id')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'db_table': 'like',
                'unique_together': {('from_id', 'post_id')},
            },
        ),
        migrations.CreateModel(
            name='PostPic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_url', models.CharField(max_length=255)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='backend.post')),
            ],
            options={
                'verbose_name': 'Post Picture',
                'verbose_name_plural': 'Post Pictures',
                'db_table': 'post_pic',
                'ordering': ['order', 'id'],
            },
        ),
    ]
