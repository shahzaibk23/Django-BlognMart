# Generated by Django 3.0.8 on 2020-07-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0014_auto_20200711_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Clothing', 'Clothing'), ('Accessories', 'Accessories')], default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
