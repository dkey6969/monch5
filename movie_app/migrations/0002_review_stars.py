# Generated by Django 5.1.4 on 2025-01-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
