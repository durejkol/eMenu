# Generated by Django 2.0.2 on 2018-04-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0005_auto_20180425_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
