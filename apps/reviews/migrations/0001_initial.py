# Generated by Django 5.0.3 on 2024-06-01 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trainer.trainer', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Отзыв ',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]