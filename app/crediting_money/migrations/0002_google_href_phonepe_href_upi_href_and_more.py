# Generated by Django 4.1.5 on 2023-02-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urls_for_ticket', '0003_alter_tempacc_url'),
        ('crediting_money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='google',
            name='href',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_for_ticket.tempacc'),
        ),
        migrations.AddField(
            model_name='phonepe',
            name='href',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_for_ticket.tempacc'),
        ),
        migrations.AddField(
            model_name='upi',
            name='href',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_for_ticket.tempacc'),
        ),
        migrations.AddField(
            model_name='withdrawalmoney',
            name='href',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_for_ticket.tempacc'),
        ),
    ]
