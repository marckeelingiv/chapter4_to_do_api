# Generated by Django 5.0.4 on 2024-04-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
