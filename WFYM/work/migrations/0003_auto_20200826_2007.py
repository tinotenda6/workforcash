# Generated by Django 3.0.4 on 2020-08-26 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20200823_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chores',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AddField(
            model_name='chores',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
