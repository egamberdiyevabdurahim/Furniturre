from django.db import models

from common.models import BaseModel
from products.models import ProductModel


class OrderModel(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderItemModel(BaseModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product.name} {self.order.id}"

    class Meta:
        verbose_name = 'order item'
        verbose_name_plural = 'order items'
