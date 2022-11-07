# Generated by Django 3.2.7 on 2022-11-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('department_intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('recruiter_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('recruiter_name', models.CharField(max_length=255)),
                ('recruiter_sex', models.BooleanField()),
                ('recruiter_age', models.IntegerField()),
                ('recruiter_target_department', models.CharField(max_length=255)),
                ('recruiter_intro', models.TextField()),
                ('recruiter_phone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=16)),
                ('reward', models.IntegerField()),
                ('record', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('worker_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('training_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('training_name', models.CharField(max_length=255)),
                ('training_intro', models.TextField()),
                ('training_place', models.CharField(max_length=255)),
                ('training_start_time', models.DateTimeField()),
                ('training_end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('usr_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('usr_password', models.CharField(max_length=25)),
                ('usr_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=255)),
                ('worker_sex', models.BooleanField()),
                ('worker_age', models.IntegerField()),
                ('worker_department', models.CharField(max_length=255)),
                ('worker_position', models.CharField(max_length=255)),
                ('worker_phone', models.CharField(max_length=16)),
                ('worker_entry_time', models.DateTimeField()),
            ],
        ),
    ]