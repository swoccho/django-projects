# Generated by Django 4.0.2 on 2022-05-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(editable=False),
        ),
    ]
