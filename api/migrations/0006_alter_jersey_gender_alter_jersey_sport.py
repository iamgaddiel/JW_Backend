# Generated by Django 4.1.3 on 2022-11-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_brand_alter_sport_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jersey',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unisex', 'unisex')], max_length=7),
        ),
        migrations.AlterField(
            model_name='jersey',
            name='sport',
            field=models.CharField(max_length=200),
        ),
    ]
