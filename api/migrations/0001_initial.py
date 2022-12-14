# Generated by Django 4.1.3 on 2022-11-07 22:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(default='user.png', upload_to='user_profile_images')),
                ('street', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('delivery_address', models.CharField(max_length=400)),
                ('delivery_address_two', models.CharField(max_length=400)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jersey',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300, unique=True)),
                ('main_image', models.ImageField(default='jersey_image.png', upload_to='jersey_images')),
                ('image_two', models.ImageField(blank=True, default='jersey_image.png', upload_to='jersey_images')),
                ('image_three', models.ImageField(blank=True, default='jersey_image.png', upload_to='jersey_images')),
                ('image_four', models.ImageField(blank=True, default='jersey_image.png', upload_to='jersey_images')),
                ('quantity', models.IntegerField(default=0)),
                ('size', models.CharField(choices=[('xs', 'xs'), ('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl'), ('xxxl', 'xxxl')], max_length=5)),
                ('is_original', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('discount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('price', models.FloatField()),
                ('is_ordered', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('billing_address', models.TextField()),
                ('sub_total', models.FloatField()),
                ('total', models.FloatField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentMethod',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('days_to_delivery', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('price', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cart')),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jersey')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='api.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment_method',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.shipmentmethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
