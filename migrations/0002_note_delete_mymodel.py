# Generated by Django 4.2.7 on 2023-12-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
