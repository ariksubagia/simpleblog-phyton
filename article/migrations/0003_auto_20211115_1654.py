# Generated by Django 3.1.1 on 2021-11-15 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='posted_by',
            new_name='poster',
        ),
    ]
