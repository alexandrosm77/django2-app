# Generated by Django 2.1.7 on 2019-04-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
