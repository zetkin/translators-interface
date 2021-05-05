# Generated by Django 3.2 on 2021-05-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0006_project_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repository_name',
            field=models.CharField(default='zetkin/default', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('repository_name', 'locale_files_path')},
        ),
        migrations.RemoveField(
            model_name='project',
            name='repository_url',
        ),
    ]
