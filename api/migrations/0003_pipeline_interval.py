# Generated by Django 4.1 on 2022-08-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_pipeline_top_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipeline',
            name='interval',
            field=models.CharField(choices=[('1', '1min'), ('5', '5min'), ('15', '15min'), ('30', '30min'), ('60', '60min')], default='5min', max_length=5),
            preserve_default=False,
        ),
    ]
