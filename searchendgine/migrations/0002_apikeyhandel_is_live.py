# Generated by Django 5.1.1 on 2024-09-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchendgine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikeyhandel',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
    ]
