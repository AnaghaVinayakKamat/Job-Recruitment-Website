# Generated by Django 3.2.6 on 2022-03-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_auto_20220312_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='cemail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]