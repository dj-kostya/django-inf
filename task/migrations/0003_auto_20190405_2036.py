# Generated by Django 2.0.13 on 2019-04-05 13:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_post_with_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TaskImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Images')),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Tasks',
        ),
        migrations.AddField(
            model_name='taskimage',
            name='id_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Tasks'),
        ),
    ]
