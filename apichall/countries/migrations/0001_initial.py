# Generated by Django 5.0.6 on 2024-07-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('countryCode', models.CharField(max_length=3)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('groupId', models.IntegerField()),
            ],
        ),
    ]
