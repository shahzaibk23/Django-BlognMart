# Generated by Django 3.0.8 on 2020-07-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20200708_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='displayImage1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='displayImage2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='displayImage3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]