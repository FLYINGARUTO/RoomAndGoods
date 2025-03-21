# Generated by Django 5.1.1 on 2025-03-15 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.IntegerField(default=0)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat Message',
                'verbose_name_plural': 'Chat Messages',
                'db_table': 'chat_message',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('is_read', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'db_table': 'notification',
                'ordering': ['-create_at'],
            },
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterUniqueTogether(
            name='collect',
            unique_together={('from_user', 'post_id')},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='to_id',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('from_user', 'post_id')},
        ),
        migrations.AddField(
            model_name='collect',
            name='from_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='collect',
            name='to_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='from_user',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='comment',
            name='to_user',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='like',
            name='from_user',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='like',
            name='to_user',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_notifications', to='backend.post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='collect',
            name='from_id',
        ),
        migrations.RemoveField(
            model_name='collect',
            name='to_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='from_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='to_id',
        ),
    ]
