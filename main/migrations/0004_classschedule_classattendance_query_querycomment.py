# Generated by Django 5.0.2 on 2024-02-12 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_date_created_course_date_modified_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date_and_time', models.DateTimeField()),
                ('end_date_and_time', models.DateTimeField()),
                ('is_repeated', models.BooleanField(default=False)),
                ('repeat_frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('venue', models.CharField(max_length=100)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cohort')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='users.imuser')),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('resolution_status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('DECLINED', 'Declined'), ('RESOLVED', 'Resolved')], default='PENDING', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_queries', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='users.imuser')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_queries', to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='QueryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_query_comment', to='users.imuser')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.query')),
            ],
        ),
    ]
