# Generated by Django 3.2.3 on 2021-05-16 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20210516_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='feedback_required',
            new_name='customer_feedback_required',
        ),
    ]
