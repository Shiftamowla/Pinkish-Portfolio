# Generated by Django 5.1.3 on 2025-01-03 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_sports_type_pic_remove_work_type_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('pic', models.ImageField(upload_to='media/pictures')),
                ('tags', models.CharField(max_length=100)),
                ('type_pic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.photosmodel')),
            ],
        ),
    ]
