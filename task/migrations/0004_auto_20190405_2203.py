# Generated by Django 2.0.13 on 2019-04-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190405_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id_task',
            field=models.IntegerField(unique=True),
        ),
    ]
