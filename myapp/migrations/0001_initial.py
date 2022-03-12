# Generated by Django 4.0 on 2022-01-17 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Can_det',
            fields=[
                ('ename', models.CharField(default=None, max_length=50)),
                ('username', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('epasswd', models.CharField(max_length=15000)),
                ('ephn', models.BigIntegerField()),
                ('edob', models.DateField()),
                ('eaddr', models.CharField(max_length=200)),
                ('ecity', models.CharField(max_length=50)),
                ('estate', models.CharField(max_length=50)),
                ('ezip', models.IntegerField()),
                ('egen', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'candidate_details',
            },
        ),
        migrations.CreateModel(
            name='Com_det',
            fields=[
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('cpasswd', models.CharField(max_length=16)),
                ('cphn', models.BigIntegerField()),
                ('caddr', models.CharField(max_length=200)),
                ('ccity', models.CharField(max_length=50)),
                ('cstate', models.CharField(max_length=50)),
                ('czip', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'company_details',
            },
        ),
        migrations.CreateModel(
            name='Job_det',
            fields=[
                ('jobid', models.AutoField(default='', editable=False, primary_key=True, serialize=False, unique=True)),
                ('jobpost', models.CharField(max_length=100)),
                ('cemail', models.EmailField(max_length=50)),
                ('cname', models.CharField(default='', max_length=50)),
                ('jobdes', models.CharField(max_length=900)),
                ('indexp', models.CharField(max_length=50)),
                ('workdays', models.CharField(max_length=50)),
                ('jskill1', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill2', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill3', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill4', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill5', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill6', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill7', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill8', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill9', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('jskill10', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('salary', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Job_Post_details',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('resid', models.AutoField(default='', editable=False, primary_key=True, serialize=False, unique=True)),
                ('git', models.URLField(blank=True, default='', null=True)),
                ('lkdn', models.URLField(blank=True, default='', null=True)),
                ('summary', models.CharField(default='', max_length=500)),
                ('iedu', models.CharField(default='', max_length=100)),
                ('dedu', models.CharField(default='', max_length=100)),
                ('pedu', models.CharField(default='', max_length=20)),
                ('sedu', models.CharField(default='', max_length=20)),
                ('workexp', models.CharField(blank=True, max_length=20, null=True)),
                ('skill1', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill2', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill3', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill4', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill5', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill6', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill7', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill8', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill9', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('skill10', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('pexp', models.URLField(blank=True, null=True)),
                ('achv', models.URLField(blank=True, null=True)),
                ('username', models.EmailField(max_length=50, unique=True)),
                ('hby1', models.CharField(default='', max_length=50)),
                ('hby2', models.CharField(default='', max_length=50)),
                ('hby3', models.CharField(default='', max_length=50)),
                ('hby4', models.CharField(default='', max_length=50)),
                ('hby5', models.CharField(default='', max_length=50)),
                ('hby6', models.CharField(default='', max_length=50)),
                ('hby7', models.CharField(default='', max_length=50)),
                ('hby8', models.CharField(default='', max_length=50)),
                ('hby9', models.CharField(default='', max_length=50)),
                ('hby10', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Apply_job',
            fields=[
                ('jobappid', models.AutoField(default='', editable=False, primary_key=True, serialize=False, unique=True)),
                ('reason', models.CharField(default='', max_length=900)),
                ('job', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapp.job_det')),
            ],
        ),
    ]
