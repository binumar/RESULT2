# Generated by Django 5.1.3 on 2024-12-06 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_teacherprofile_level_studentprofile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formmasterprofile',
            name='subject',
        ),
        migrations.AddField(
            model_name='formmasterprofile',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.level'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_form_master',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
