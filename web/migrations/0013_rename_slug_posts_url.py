# Generated by Django 4.2.6 on 2023-11-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_posts_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='slug',
            new_name='url'

        ),
    ]