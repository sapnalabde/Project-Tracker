# Generated by Django 4.0.3 on 2022-04-15 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project_Management', '0010_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='m2',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='m2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
