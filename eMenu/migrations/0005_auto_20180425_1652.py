# Generated by Django 2.0.2 on 2018-04-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0004_auto_20180424_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
