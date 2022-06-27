# Generated by Django 4.0.3 on 2022-03-30 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('client_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('creator', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=100)),
                ('priority', models.IntegerField(blank=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1, null=True)),
                ('project_type', models.IntegerField(blank=True, choices=[(1, 'POC'), (2, 'PO'), (3, 'ECIF'), (4, 'DEMO')], default=1, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('approval_status', models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Rejected')], default=1, null=True)),
                ('project_status', models.IntegerField(blank=True, choices=[(1, 'Initiated'), (2, 'On going'), (3, 'On Hold'), (4, 'Completed')], default=1, null=True)),
                ('attachment', models.FileField(upload_to='media')),
                ('assignted_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to=settings.AUTH_USER_MODEL)),
                ('vertical', models.ManyToManyField(blank=True, to='accounts.vertical')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creater', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('task_type', models.IntegerField(blank=True, choices=[(1, 'Internal Meeting'), (2, 'External Meeting'), (3, 'Training'), (4, 'Task')], default=1, null=True)),
                ('task_description', models.TextField(blank=True, null=True)),
                ('task_status', models.IntegerField(blank=True, choices=[(0, 'Initiated'), (1, 'In progress'), (3, 'Completed')], default=1, null=True)),
                ('effort_hours', models.TimeField()),
                ('Collaborated_with', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project_Management.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('attachment', models.FileField(upload_to='media')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project_Management.project')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
