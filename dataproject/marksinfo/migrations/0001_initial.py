# Generated by Django 3.1.1 on 2022-12-17 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('studentid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
