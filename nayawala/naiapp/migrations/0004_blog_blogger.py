# Generated by Django 3.0.8 on 2020-07-10 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
        ('naiapp', '0003_auto_20200710_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogger.Blogger'),
        ),
    ]
