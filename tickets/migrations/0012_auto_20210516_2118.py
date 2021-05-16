# Generated by Django 3.2.3 on 2021-05-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20210516_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='feedback_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='hours_predicted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ticket',
            name='hours_used',
            field=models.FloatField(default=0),
        ),
    ]
