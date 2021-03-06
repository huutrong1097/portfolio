# Generated by Django 3.2.8 on 2021-10-11 16:05

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20211009_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
