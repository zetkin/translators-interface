# Generated by Django 3.2 on 2021-06-03 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0011_alter_translation_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='last_sync_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]