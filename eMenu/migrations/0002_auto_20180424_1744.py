# Generated by Django 2.0.2 on 2018-04-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='preparation_time',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
