# Generated by Django 3.2.3 on 2021-05-16 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_feedback_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback_request',
            new_name='FeedbackRequest',
        ),
    ]