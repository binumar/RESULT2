# Generated by Django 5.1.3 on 2024-12-06 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='level',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='house',
            field=models.CharField(blank=True, choices=[('ABIOLA', 'ABIOLA'), ('AHMAD LAWAN', 'AHMAD LAWAN'), ('JUSTICE ALOOMA', 'JUSTICE ALOOMA'), ('NGOZI OKONJU NWELA', 'NGOZI OKONJU NWELA'), ('GOODLUCK EBELE JONATHAN', 'GOODLUCK EBELE JONATHAN')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.subject'),
        ),
        migrations.AddField(
            model_name='term',
            name='closes_on',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='FormMasterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_number', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=1000)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.subject')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fmprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
