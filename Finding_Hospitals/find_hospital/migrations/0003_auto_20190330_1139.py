# Generated by Django 2.1.7 on 2019-03-30 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('find_hospital', '0002_remove_find_hosp_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='find_hosp',
            old_name='text',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='find_hosp',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='find_hosp',
            name='contact',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='find_hosp',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='find_hosp',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]