from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    phone = models.CharField(max_length=20, unique=True)
    image = models.ImageField(default='user.png', upload_to='user_profile_images')
    street = models.CharField(max_length=400)
    country = models.CharField(max_length=400)
    email = models.EmailField(unique=True)
    email_is_verified = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=400)
    delivery_address_two = models.CharField(max_length=400)
    delivery_address_two = models.CharField(max_length=400)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.username


class Sport_Category(models.Model):
    class Meta:
        verbose_name_plural = 'sport Categories'

    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Brand(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    title = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.title


class Jersey(models.Model):
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
        ('unisex', 'unisex'),
    ]
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    title = models.CharField(max_length=200, unique=True)
    main_image = models.ImageField(upload_to="jersey_images", default="jersey_image.png")
    image_two = models.ImageField(upload_to="jersey_images", default="jersey_image.png", blank=True)
    image_three = models.ImageField(upload_to="jersey_images", default="jersey_image.png", blank=True)
    image_four = models.ImageField(upload_to="jersey_images", default="jersey_image.png", blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Sport_Category, null=True  ,on_delete=models.CASCADE)
    sport = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=7, choices=GENDER)
    is_original = models.BooleanField(default=False)
    price = models.FloatField()
    description = models.TextField()
    discount = models.FloatField()
    # rating = models.DecimalField() #TOdO add this later
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



class ShipmentMethod(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    name = models.CharField(max_length=50, unique=True)
    days_to_delivery = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name


class OrderItem(models.Model):
    SIZE = [
        ('xs', 'xs'),
        ('s', 's'),
        ('m', 'm'),
        ('l', 'l'),
        ('xl', 'xl'),
        ('xxl', 'xxl'),
        ('xxxl', 'xxxl'),
    ]
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    session_id = models.UUIDField(editable=False, unique=True, default=uuid4, blank=True, null=True)
    jersey = models.ForeignKey(Jersey, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    size = models.CharField(choices=SIZE, max_length=5)
    customize = models.BooleanField(default=False)
    custom_player = models.CharField(max_length=255)
    custom_user_number = models.CharField(max_length=4, blank=True)
    custom_user_name = models.CharField(max_length=50, blank=True)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.FloatField()
    order_item = models.ManyToManyField(OrderItem)
    shipment_method = models.ForeignKey(ShipmentMethod, on_delete=models.CASCADE, blank=True)
    is_ordered = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    billing_address = models.TextField()
    sub_total = models.FloatField()
    total = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return super().__str__()


class Cart(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    order_item = models.ManyToManyField(OrderItem)
    session_id = models.UUIDField(editable=False, unique=True, default=uuid4, blank=True, null=True)

    
    def __str__(self) -> str:
        return '{user} cart'.format(user=self.user.username)


class Transactions(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.FloatField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return super().__str__()



