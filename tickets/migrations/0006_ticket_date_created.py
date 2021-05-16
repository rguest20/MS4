# Generated by Django 3.2.3 on 2021-05-16 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Created'),
            preserve_default=False,
        ),
    ]
