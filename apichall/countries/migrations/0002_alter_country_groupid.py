# Generated by Django 5.0.6 on 2024-07-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='groupId',
            field=models.IntegerField(default=0),
        ),
    ]
