# Generated by Django 3.0.8 on 2020-07-08 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('summary', models.TextField()),
                ('datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Category1', 'Restaurant food '), ('Category2', 'Travel news '), ('Category3', 'Modern technology '), ('Category4', 'Product '), ('Category5', 'Inspiration '), ('Category6', 'health care')], default='--', max_length=120)),
            ],
        ),
    ]