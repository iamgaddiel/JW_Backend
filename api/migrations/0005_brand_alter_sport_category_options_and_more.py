# Generated by Django 4.1.3 on 2022-11-18 18:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_sport_sport_category_jersey_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sport_category',
            options={'verbose_name_plural': 'sport Categories'},
        ),
        migrations.RemoveField(
            model_name='jersey',
            name='size',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_item',
            field=models.ManyToManyField(to='api.orderitem'),
        ),
        migrations.AddField(
            model_name='jersey',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='unisex', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jersey',
            name='sport',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='custom_player',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='custom_user_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='custom_user_number',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='customize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('xs', 'xs'), ('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl'), ('xxxl', 'xxxl')], default='M', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jersey',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.brand'),
        ),
    ]
