# Generated by Django 4.1.5 on 2023-01-10 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_alter_message_options_chat_createdate_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='chat',
            name='createdate',
        ),
        migrations.RemoveField(
            model_name='message',
            name='createdate',
        ),
    ]