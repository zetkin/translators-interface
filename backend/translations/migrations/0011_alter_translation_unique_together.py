# Generated by Django 3.2 on 2021-05-08 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0010_alter_translation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('file_path', 'object_path', 'created_at', 'project')},
        ),
    ]