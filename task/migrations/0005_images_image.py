# Generated by Django 2.0.13 on 2019-04-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190405_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default=' ', null=True, upload_to='static/img/%Y/%m/%d/'),
        ),
    ]