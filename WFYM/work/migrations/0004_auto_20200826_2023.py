# Generated by Django 3.0.4 on 2020-08-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20200826_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alltask',
            name='date_or_time_due',
            field=models.DateTimeField(blank=True, default='timezone.now'),
        ),
    ]
