# Generated by Django 3.2 on 2021-06-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0014_auto_20210611_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(help_text='Make sure to always select English, and any other translations in this project.', to='translations.Language'),
        ),
    ]
