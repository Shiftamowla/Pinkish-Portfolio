# Generated by Django 5.1.3 on 2025-01-03 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_food_photograph_sports_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photosmodel',
            name='description',
        ),
    ]