# Generated by Django 4.0.3 on 2022-04-14 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project_Management', '0008_remove_projectteam_team_projectteam_team_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectteam',
            old_name='team',
            new_name='assign_to',
        ),
        migrations.RenameField(
            model_name='projectteam',
            old_name='description',
            new_name='remark',
        ),
        migrations.RemoveField(
            model_name='project',
            name='assignted_to',
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
