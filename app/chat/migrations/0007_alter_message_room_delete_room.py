# Generated by Django 4.1.5 on 2023-01-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
