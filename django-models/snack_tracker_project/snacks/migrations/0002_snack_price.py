# Generated by Django 4.0.4 on 2022-05-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
