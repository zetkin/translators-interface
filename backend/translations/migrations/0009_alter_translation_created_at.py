# Generated by Django 3.2 on 2021-05-06 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0008_auto_20210505_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
