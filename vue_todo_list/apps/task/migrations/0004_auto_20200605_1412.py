# Generated by Django 3.0.7 on 2020-06-05 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20200605_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='sub_task',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.Task'),
        ),
    ]
