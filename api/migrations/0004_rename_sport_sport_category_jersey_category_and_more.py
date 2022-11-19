# Generated by Django 4.1.3 on 2022-11-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_cart_id_alter_jersey_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sport',
            new_name='Sport_Category',
        ),
        migrations.AddField(
            model_name='jersey',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sport_category'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_is_verified',
            field=models.BooleanField(default=False),
        ),
    ]