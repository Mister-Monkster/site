# Generated by Django 4.2.6 on 2023-11-25 17:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_posts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True, verbose_name='URL'),
        ),
    ]