# Generated by Django 3.2 on 2021-05-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0003_translation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translation',
            old_name='from_repo',
            new_name='from_repository',
        ),
        migrations.AlterField(
            model_name='translation',
            name='text',
            field=models.TextField(default='hewwo'),
            preserve_default=False,
        ),
    ]
