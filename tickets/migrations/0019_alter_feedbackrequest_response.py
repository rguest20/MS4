# Generated by Django 3.2.3 on 2021-05-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0018_alter_feedbackrequest_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackrequest',
            name='response',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
