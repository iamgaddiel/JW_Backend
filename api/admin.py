from django.contrib import admin

from .models import (
    Jersey,
    User,
    Cart,
    Order,
    OrderItem,
    ShipmentMethod,
    Sport_Category,
    Transactions,
    Brand
)


admin.site.register(User)
admin.site.register(Jersey)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShipmentMethod)
admin.site.register(Transactions)
admin.site.register(Sport_Category)
admin.site.register(Brand)
