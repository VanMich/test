# Generated by Django 4.0.4 on 2022-07-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
    ]
