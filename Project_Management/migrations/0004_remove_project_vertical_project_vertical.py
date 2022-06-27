# Generated by Django 4.0.3 on 2022-04-05 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_userrole'),
        ('Project_Management', '0003_project_csowner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='vertical',
        ),
        migrations.AddField(
            model_name='project',
            name='vertical',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.vertical'),
            preserve_default=False,
        ),
    ]
