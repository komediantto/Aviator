# Generated by Django 4.1.5 on 2023-01-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls_for_ticket', '0002_alter_tempacc_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempacc',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]