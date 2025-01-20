# Generated by Django 5.1.4 on 2025-01-12 05:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0006_alter_jobfile_job_file_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobfile",
            name="job_file_number",
            field=models.CharField(
                default=django.utils.timezone.now, max_length=100, unique=True
            ),
            preserve_default=False,
        ),
    ]
