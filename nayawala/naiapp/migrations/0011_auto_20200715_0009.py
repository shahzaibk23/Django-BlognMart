# Generated by Django 3.0.8 on 2020-07-14 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naiapp', '0010_auto_20200714_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Title',
            new_name='cat_title',
        ),
    ]
