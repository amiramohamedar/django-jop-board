# Generated by Django 4.1.7 on 2023-02-28 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_category_rename_vacancy_job_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
    ]