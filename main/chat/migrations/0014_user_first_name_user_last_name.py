# Generated by Django 4.1.5 on 2023-01-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_alter_chat_author_alter_message_chat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
