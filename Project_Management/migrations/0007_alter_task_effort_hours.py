# Generated by Django 4.0.3 on 2022-04-08 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Management', '0006_alter_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='effort_hours',
            field=models.IntegerField(max_length=10),
        ),
    ]
