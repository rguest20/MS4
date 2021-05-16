# Generated by Django 3.2.3 on 2021-05-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contracted_monthly_sem_hours',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='contracted_monthly_service_hours',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='client',
            name='paid_extra_hours',
            field=models.FloatField(default=0),
        ),
    ]