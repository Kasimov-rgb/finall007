# Generated by Django 5.0.3 on 2024-06-08 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_trainer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='photo',
        ),
    ]
