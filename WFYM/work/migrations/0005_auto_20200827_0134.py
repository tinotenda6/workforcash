# Generated by Django 3.0.4 on 2020-08-27 01:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20200826_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alltask',
            name='date_or_time_due',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]