# Generated by Django 4.1 on 2022-09-27 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
