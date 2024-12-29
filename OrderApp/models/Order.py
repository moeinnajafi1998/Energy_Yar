from django.db import models
from .CustomUser import CustomUser

class Order(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(CustomUser, to_field='username',on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f'{self.product_name} - {self.customer.username}'
