# Generated by Django 3.2.3 on 2021-05-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.TextField(),
        ),
    ]
