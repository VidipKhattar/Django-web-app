# Generated by Django 4.0.3 on 2022-03-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardenGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingoftheday',
            name='reward',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
