# Generated by Django 3.2.20 on 2023-07-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
