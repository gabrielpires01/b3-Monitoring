# Generated by Django 4.1 on 2022-08-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pipeline_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='interval',
            field=models.CharField(choices=[('1min', '1min'), ('5min', '5min'), ('15min', '15min'), ('30min', '30min'), ('60min', '60min')], max_length=5),
        ),
    ]
