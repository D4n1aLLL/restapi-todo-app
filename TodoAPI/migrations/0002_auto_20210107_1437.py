# Generated by Django 3.1.5 on 2021-01-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateCompleted',
            field=models.DateTimeField(blank=True),
        ),
    ]
