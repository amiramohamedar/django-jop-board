# Generated by Django 4.1.7 on 2023-02-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]