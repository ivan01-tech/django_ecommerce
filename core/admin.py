from django.contrib import admin
from core.models import Item, Order, OrderItem

# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)