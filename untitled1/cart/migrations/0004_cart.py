# Generated by Django 3.0.8 on 2020-07-14 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_remove_seller_about'),
        ('cart', '0003_auto_20200714_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.CartItem')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
    ]