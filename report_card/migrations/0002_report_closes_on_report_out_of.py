# Generated by Django 5.1.3 on 2024-12-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='closes_on',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='out_of',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
