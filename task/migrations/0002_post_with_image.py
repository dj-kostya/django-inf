# Generated by Django 2.0.13 on 2019-04-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='with_image',
            field=models.BooleanField(default=False),
        ),
    ]