# Generated by Django 4.1.4 on 2023-04-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_task_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.IntegerField(primary_key=int, serialize=False),
        ),
    ]
