# Generated by Django 3.2.6 on 2022-01-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_apply_job_ephn'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_job',
            name='comemail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
