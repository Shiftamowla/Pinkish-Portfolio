# Generated by Django 5.1.3 on 2025-01-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='photosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('pic', models.ImageField(upload_to='media/pictures')),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
