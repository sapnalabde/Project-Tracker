# Generated by Django 4.0.3 on 2022-04-15 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project_Management', '0013_alter_teammember_m2_alter_teammember_m3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='m2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userm2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='m3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userm3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='m4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userm4', to=settings.AUTH_USER_MODEL),
        ),
    ]