from django.contrib import admin

from orders.models import OrderModel, OrderItemModel

admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
