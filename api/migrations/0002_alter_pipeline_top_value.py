# Generated by Django 4.1 on 2022-08-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='top_value',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
