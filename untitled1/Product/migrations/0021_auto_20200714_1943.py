# Generated by Django 3.0.8 on 2020-07-14 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0020_auto_20200714_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.Categories'),
        ),
    ]