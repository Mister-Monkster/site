# Generated by Django 4.2.6 on 2024-02-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_alter_posts_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban_words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, verbose_name='Слово')),
            ],
        ),
    ]
